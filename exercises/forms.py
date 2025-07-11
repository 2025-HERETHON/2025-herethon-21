from django import forms
from .models import ExerciseReview

class ExerciseReviewForm(forms.ModelForm):
    class Meta:
        model = ExerciseReview
        fields = ('exercise_history','rating','comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance', None) is not None:
            self.fields.pop('exercise_history')