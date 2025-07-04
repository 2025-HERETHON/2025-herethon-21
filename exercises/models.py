from django.db import models
from utils.choices import ExerciseCategoryType

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
