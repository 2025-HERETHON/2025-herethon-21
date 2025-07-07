from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .services import UserService
from .forms import CustomUserCreationForm, CustomUserChangeForm
from utils.choices import ExerciseGoalType
from django.http import HttpResponseForbidden
from .models import CustomUser
from .services import UserService

# 템플릿 렌더링 처리

def main_view(request):
    goal_labels = []
    if request.user.is_authenticated:
        goals = request.user.exercise_goal  # ["1", "2", "4"]
        goal_labels = [ExerciseGoalType(int(g)).label for g in goals] # -> [1, 2, 4]
    
    return render(request, "main.html", {
        "goal_labels": goal_labels,
    })


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = UserService.signup(form)   # form 그대로 넘김, clean_data만 넘길 시 폼 기능 못 씀
                return redirect("accounts:login")
            except ValidationError as e:
                return render(request, "signup.html", {"form": form, "error": str(e)})
        else:
            return render(request, "signup.html", {"form": form, "error": "입력값을 확인해주세요."})
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

     
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
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
    
def update_CustomUser(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.user != user:
        return HttpResponseForbidden("권한이 없습니다.")

    if request.method == "POST":
        form, success = UserService.update(user, request.POST, request.FILES)
        if success:
            return redirect("accounts:main")
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, "update.html", {"form": form, "user": user})