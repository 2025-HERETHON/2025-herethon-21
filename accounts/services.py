# 백엔드 비즈니스 로직 처리

from django.core.exceptions import ValidationError
from .forms import CustomUserCreationForm

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
