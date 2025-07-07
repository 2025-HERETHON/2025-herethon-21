from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm, SetUnusablePasswordMixin
from .models import CustomUser
from utils.choices import ExerciseGoalType
from django import forms


class CustomBaseUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
        read_only_fields = ("username",)

class CustomUserCreationForm(CustomBaseUserCreationForm):
    exercise_goal = forms.MultipleChoiceField(
        choices=ExerciseGoalType.choices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(CustomBaseUserCreationForm.Meta):
        fields = CustomBaseUserCreationForm.Meta.fields + ("exercise_goal","profile_image",)

class CustomUserChangeForm(UserChangeForm):
    exercise_goal = forms.MultipleChoiceField(
        choices=ExerciseGoalType.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = CustomUser
        fields = ("email", "profile_image", "exercise_goal", "bio")
        read_only_fields = ("username",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial.get("exercise_goal"):
            self.initial["exercise_goal"] = list(map(int, self.initial["exercise_goal"]))

class CustomAdminUserCreationForm(SetUnusablePasswordMixin, CustomBaseUserCreationForm):
    usable_password = SetUnusablePasswordMixin.create_usable_password_field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].required = False
        self.fields["password2"].required = False