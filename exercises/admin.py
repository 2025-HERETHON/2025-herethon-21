from django.contrib import admin
from .models import Exercise, ExerciseHistory, ExerciseReview, ReactedExerciseReview, ScrappedExerciseRoutine

admin.site.register(Exercise)
admin.site.register(ExerciseHistory)
admin.site.register(ExerciseReview)
admin.site.register(ReactedExerciseReview)
admin.site.register(ScrappedExerciseRoutine)