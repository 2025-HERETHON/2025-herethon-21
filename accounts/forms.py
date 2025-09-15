from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm, SetUnusablePasswordMixin
from .models import CustomUser
from django import forms
from django.contrib.auth import get_user_model

class CustomBaseUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("id","email",)
        read_only_fields = ("id",)

class CustomUserCreationForm(CustomBaseUserCreationForm):
    class Meta(CustomBaseUserCreationForm.Meta):
        fields = CustomBaseUserCreationForm.Meta.fields + ("nickname","bio","profile_image","exercise_goal",)
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = ("id",)

class CustomAdminUserCreationForm(SetUnusablePasswordMixin, CustomBaseUserCreationForm):
    usable_password = SetUnusablePasswordMixin.create_usable_password_field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].required = False
        self.fields["password2"].required = False
