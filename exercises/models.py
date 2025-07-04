from django.db import models
from utils.mixins import JSONIntListHandler
from utils.choices import ExerciseCategoryType
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
