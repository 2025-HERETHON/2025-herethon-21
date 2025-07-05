# 백엔드 비즈니스 로직 처리

from django.core.exceptions import ValidationError
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate

class UserService:
    @staticmethod
    def signup(data):
        form = CustomUserCreationForm(data)
        if form.is_valid():
            user = form.save()
            return user
        else:
            # 폼의 에러를 JSON으로
            raise ValidationError(form.errors.as_json())

class UserService:
    @staticmethod
    def login(data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise ValidationError("이메일과 비밀번호는 필수 항목입니다.")

        user = authenticate(username=email, password=password)
        if user is None:
            raise ValidationError("이메일 또는 비밀번호가 올바르지 않습니다.")

        return user