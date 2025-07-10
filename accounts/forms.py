from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm, SetUnusablePasswordMixin
from .models import CustomUser
from utils.choices import ExerciseGoalType
from django import forms
from django.contrib.auth import get_user_model



class CustomBaseUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
        read_only_fields = ("username",)

class CustomUserCreationForm(CustomBaseUserCreationForm):
    nickname = forms.CharField(max_length=100, required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_image = forms.ImageField(required=False)
    exercise_goal = forms.MultipleChoiceField(
        choices=ExerciseGoalType.choices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(CustomBaseUserCreationForm.Meta):
        fields = CustomBaseUserCreationForm.Meta.fields + ("exercise_goal","profile_image", "nickname", "bio")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['email'].required = False
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            self.fields['password1'].widget = forms.HiddenInput()
            self.fields['password2'].widget = forms.HiddenInput()

    def clean_email(self):
        if self.instance and self.instance.pk:
            return self.instance.email
        return self.cleaned_data['email']

    def save(self, commit=True):
        User = get_user_model()
        user = self.instance if self.instance.pk else User()

        # 필드 할당
        for field in self.Meta.fields:
            if field in self.cleaned_data:
                setattr(user, field, self.cleaned_data[field])

        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)

        # 이미지 없는 경우만 기본 이미지 적용
        # 이미 새 이미지가 들어왔으면 그대로 두기
        if not user.profile_image or not getattr(user.profile_image, 'name', None):
            user.profile_image = 'user/profile_image/default.jpg'

        if commit:
            user.save()

        return user
    
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