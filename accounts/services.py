# 백엔드 비즈니스 로직 처리

from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from utils.json_handlers import JSONIntChoicesListHandler
from utils.choices import ExerciseGoalType



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

        user = authenticate(request, email=email, password=password)

        if user is None:
            User = get_user_model()
            try:
                found_user = User.objects.get(email=email)
            except User.DoesNotExist:
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
        print("🔵 [SERVICE] update() 진입")
        form = CustomUserCreationForm(form_data, files_data, instance=user)

        if form.is_valid():
            instance = form.save(commit=False)

            goals = form_data.getlist("goals")
            print("🎯 선택된 goals (문자열):", goals)

            goal_ints = [int(g) for g in goals if g.isdigit()]
            print("🎯 변환된 goals (정수):", goal_ints)

            JSONIntChoicesListHandler(instance, "exercise_goal", ExerciseGoalType).set(goal_ints, save=False)

            instance.save()
            print("✅ [SERVICE] 사용자 정보 저장 완료")
            return form, True

        print("❌ [SERVICE] form 유효성 실패")
        print("🔎 form.errors:", form.errors)
        return form, False
