from django.contrib import admin
from .models import Exercise, ExerciseHistory, ExerciseReview, ReactedExerciseReview

admin.site.register(Exercise)
admin.site.register(ExerciseHistory)
admin.site.register(ExerciseReview)
admin.site.register(ReactedExerciseReview)
