from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from utils.choices import ExerciseCategoryType, ReactionEmojiType
from accounts.models import CustomUser

class Exercise(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )
    duration = models.DurationField()
    category = models.PositiveSmallIntegerField(
        choices=ExerciseCategoryType.choices
    )
    description = models.TextField()
    image1 = models.ImageField(
        upload_to='exercise/image',
    )
    image2 = models.ImageField(
        upload_to='exercise/image',
    )
    image3 = models.ImageField(
        upload_to='exercise/image',
    )

    def __str__(self):
        return self.name

class ExerciseHistory(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='exercise_histories',
        on_delete=models.CASCADE,
    )
    exercise_routine_duration = models.DurationField()

    def __str__(self):
        return f'[{self.user.email}] {self.created_at}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','created_at'],
                name='unique_user_created_at',
                violation_error_message='사용자는 같은 시간에 운동을 동시에 할 수 없습니다.',
            )
        ]
        ordering = ['created_at']

class ExerciseReview(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    exercise_history = models.OneToOneField(
        ExerciseHistory,
        related_name='exercise_review',
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    comment = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'[{self.exercise_history.user.email}] {self.exercise_history.created_at}'

class ReactedExerciseReview(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='reacted_exercise_reviews',
        on_delete=models.CASCADE,
    )
    exercise_review = models.ForeignKey(
        ExerciseReview,
        related_name='reactions',
        on_delete=models.CASCADE,
    )
    emoji = models.PositiveSmallIntegerField(
        choices=ReactionEmojiType.choices,
    )

    def __str__(self):
        return f'[{self.user.email}] {self.exercise_review}, {ReactionEmojiType(self.emoji).label}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','exercise_review'],
                name='unique_user_exercise_review',
                violation_error_message='사용자는 운동 리뷰 반응을 한 개만 남길 수 있습니다.',
            )
        ]
        ordering = ['emoji']

class ScrappedExerciseRoutine(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name='scrapped_exercise_routines',
        on_delete=models.CASCADE,
    )
    scrapped_at = models.DateTimeField()
    order = models.PositiveSmallIntegerField(
        db_index=True, # 정렬 성능 개선
    )
    exercise = models.ForeignKey(
        Exercise,
        related_name='scrapped_exercise_routines',
        on_delete=models.RESTRICT,
    )
    difficulty = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'[{self.user.email}] {self.scrapped_at}/{self.order}.{self.exercise.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','scrapped_at','order'],
                name='unique_user_scrapped_at_order',
                violation_error_message='사용자의 운동 루틴은 순번을 중복해서 가질 수 없습니다.',
            )
        ]
        ordering = ['-scrapped_at','order']