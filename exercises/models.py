from django.core.validators import MaxValueValidator
from django.db import models
from utils.mixins import JSONIntListHandler
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
    image = models.ImageField(
        upload_to='exercise/image',
    )
    description = models.TextField()

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
    exercise_routine = models.JSONField(
        default=list # list[int]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercise_routine_handler = JSONIntListHandler(
            self,
            'exercise_routine',
        )

    def __str__(self):
        return f'{self.user.email}: {self.created_at}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','created_at'],
                name='사용자는 운동을 같은 시각에 한 번만 합니다.',
            )
        ]

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
        validators=[MaxValueValidator(5)],
    )
    comment = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.exercise_history.user.email}: {self.exercise_history.created_at}'

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
        return f'{self.user.email}: {ReactionEmojiType(self.emoji).label}-{self.exercise_review}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','exercise_review'],
                name='사용자는 운동 리뷰 반응을 한 번만 남깁니다.',
            )
        ]

class ScrappedExerciseRoutine(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='scrapped_exercise_routines',
        on_delete=models.CASCADE,
    )
    exercise_routine = models.JSONField(
        default=list # list[int]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercise_routine_handler = JSONIntListHandler(
            self,
            'exercise_routine',
        )

    def __str__(self):
        return f'{self.user.email}: {self.exercise_routine}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','exercise_routine'],
                name='사용자는 동일한 운동 루틴을 한 번만 스크랩합니다.',
            )
        ]