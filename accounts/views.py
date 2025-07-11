from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .services import UserService
from .forms import CustomUserCreationForm
from utils.choices import ExerciseGoalType
from .services import UserService
from django.core.cache import cache


# 템플릿 렌더링 처리
    
def signup_onboarding1(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pw1 = request.POST.get("password1")
        pw2 = request.POST.get("password2")
        
        # 닉네임 = 이메일 기본값
        nickname = email

        session_key = request.session.session_key or request.session.save()

        cache.set(f"signup_email_{session_key}", email)
        cache.set(f"signup_pw1_{session_key}", pw1)
        cache.set(f"signup_pw2_{session_key}", pw2)
        cache.set(f"signup_nickname_{session_key}", nickname)

        return redirect("frontend:onboarding_2")
    
from django.core.exceptions import ValidationError

def signup_onboarding3_submit(request):
    if request.method == "POST":
        session_key = request.session.session_key

        # POST 복사해서 QueryDict 유지
        post_data = request.POST.copy()

        # 캐시 값 덮어쓰기
        post_data["email"] = cache.get(f"signup_email_{session_key}")
        post_data["password1"] = cache.get(f"signup_pw1_{session_key}")
        post_data["password2"] = cache.get(f"signup_pw2_{session_key}")
        post_data["nickname"] = cache.get(f"signup_nickname_{session_key}")

        # exercise_goal은 그대로 두면 됨 (checkbox로 넘어온 값은 이미 POST에 있음)

        # form 생성 (QueryDict 그대로 사용)
        form = CustomUserCreationForm(post_data)

        if form.is_valid():
            try:
                user = UserService.signup(form)
                return redirect("frontend:onboarding_3")
            except ValidationError as e:
                print("회원가입 실패:", e)
                return redirect("frontend:signuppage")
        else:
            print("폼 에러:", form.errors)
            return redirect("frontend:signuppage")



     
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not email or not password:
            raise ValidationError("이메일과 비밀번호를 모두 입력해주세요.")
        
        try:
            user = UserService.login(request, email, password)
            return redirect("accounts:main")
        except ValidationError as e:
            form = AuthenticationForm()
            # 로그인 실패 시, 에러 메시지와 함께 로그인 페이지 다시 렌더링
            return render(request, "login.html", 
                          {"form": form, "error": str(e)})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
            

def logout_view(request):
    if not request.user.is_authenticated:
        # 비로그인 상태면 로그인 화면으로 돌려보내기
        return redirect('accounts:login')
    
    logout(request)
    return redirect('accounts:login')

def delete_CustomUser(request):
    if request.method == "POST":
        try:
            UserService.delete(request.user)
            logout(request)
            return redirect("accounts:login")  # 탈퇴 후 로그인 페이지
        except ValidationError:
            return redirect("accounts:login")
    else:
        return redirect("accounts:main")

def update_CustomUser(request):
    if request.method == "POST":
        form, success = UserService.update(request.user, request.POST, request.FILES)
        if success:
            return redirect("accounts:main")
    else:
        # 폼을 새로 불러올 때 사용자 기존 정보가 담겨 있게 수정
        # 폼 변경
        form = CustomUserCreationForm(instance=request.user)
    return render(request, "update.html", {"form": form})