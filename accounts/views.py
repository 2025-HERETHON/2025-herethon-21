from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.views.decorators.http import require_POST
from menstruations.services import MenstruationService
from .models import CustomUser
from .forms import CustomUserCreationForm
from .services import UserService

# 템플릿 렌더링 처리
@require_POST
def signup_onboarding1(request:HttpRequest):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.nickname = request.POST.get("email")
        user.save()
        login(request, user)
        return redirect("frontend:onboarding_2")

def signup_onboarding2(request:HttpRequest):
    if request.method == "POST":
        service = MenstruationService(request)
        message = service.post()
        messages.success(request, message)
        return redirect("frontend:purposepage")  # ✅ 다음 온보딩 단계
    return render(request, "pages/onboarding_pages/last_menstruation_page.html")

@require_POST
def signup_onboarding3_submit(request:HttpRequest):
    exercise_goal_str = request.POST.getlist('exercise_goal')
    exercise_goal = [int(x) for x in exercise_goal_str]
    user:CustomUser = request.user
    user.exercise_goal_handler.set(exercise_goal)
    return redirect("frontend:cyclepage")
     
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not email or not password:
            raise ValidationError("이메일과 비밀번호를 모두 입력해주세요.")
        
        try:
            user = UserService.login(request, email, password)
            login(request, user)
            return redirect("frontend:mypagemain")
        except ValidationError as e:
            form = AuthenticationForm()
            # 로그인 실패 시, 에러 메시지와 함께 로그인 페이지 다시 렌더링
            return render(request, "pages/onboarding_pages/login_page.html", 
                          {"form": form, "error": str(e)})
    else:
        form = AuthenticationForm()
    return render(request, "pages/onboarding_pages/login_page.html", {"form": form})
            

def logout_view(request):
    if not request.user.is_authenticated:
        # 비로그인 상태면 로그인 화면으로 돌려보내기
        return redirect('frontend:loginpage')
    
    logout(request)
    return redirect('frontend:loginpage')

def delete_CustomUser(request):
    if request.method == "POST":
        try:
            UserService.delete(request.user)
            logout(request)
            return redirect("frontend:loginpage")  # 탈퇴 후 로그인 페이지
        except ValidationError:
            return redirect("frontend:loginpage")
    else:
        return redirect("frontend:mypagemain")

def update_CustomUser(request):
    if request.method == "POST":
        print("🔵 [DEBUG] POST 요청 수신됨")
        print("📦 POST 데이터:", dict(request.POST))
        print("📎 FILES 데이터:", dict(request.FILES))

        form, success = UserService.update(request.user, request.POST, request.FILES)

        if not success:
            print("❌ [DEBUG] form.is_valid() 실패")
            print("🧾 form.errors:", form.errors)

        if success:
            print("✅ [DEBUG] 저장 성공!")
            return redirect("frontend:mypagemain")
    else:
        form = CustomUserCreationForm(instance=request.user)
        print("🟡 [DEBUG] GET 요청 - 초기 폼 렌더링")

    return render(request, "pages/edit_page.html", {"form": form})
