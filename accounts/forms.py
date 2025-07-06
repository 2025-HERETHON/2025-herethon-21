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
    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = ("username",)

class CustomAdminUserCreationForm(SetUnusablePasswordMixin, CustomBaseUserCreationForm):
    usable_password = SetUnusablePasswordMixin.create_usable_password_field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].required = False
        self.fields["password2"].required = False