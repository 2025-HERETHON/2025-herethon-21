# 백엔드 비즈니스 로직 처리

from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm

class UserService:
    @staticmethod
    def signup(form):
        try:
            user = form.save()
        except Exception as e:
            raise ValidationError(f"회원가입 중 오류가 발생했습니다: {str(e)}")
        return user


    @staticmethod
    def login(request, email, password):
        if not email or not password:
            raise ValidationError("이메일과 비밀번호를 모두 입력해주세요.")
        
        user = authenticate(username=email, password=password)
        if user is None:
            raise ValidationError("이메일 또는 비밀번호가 올바르지 않습니다.")
        
        auth_login(request, user)
        return user

    @staticmethod
    def delete(user):
        if not user.is_authenticated:
            raise ValidationError("로그인이 필요합니다.")
        
        user.delete()
        
    @staticmethod
    def update(user, form_data, files_data=None):
        form = CustomUserCreationForm(form_data, files_data, instance=user)
        if form.is_valid():
            form.save()
            return form, True
        return form, False