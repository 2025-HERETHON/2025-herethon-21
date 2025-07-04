from django.contrib import admin
from .models import Exercise, ExerciseHistory, ExerciseReview

admin.site.register(Exercise)
admin.site.register(ExerciseHistory)
admin.site.register(ExerciseReview)
