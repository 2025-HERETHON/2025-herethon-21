from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .services import UserService
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json


# 템플릿 렌더링 처리

def main_view(request):
    if request.method == "POST":
        # 로그아웃 버튼 눌렀을 때
        if request.user.is_authenticated:
            logout(request)
            return redirect("accounts:login")  # 로그아웃 후 로그인 페이지로
        else:
            return redirect("accounts:login")
    
    # GET 요청이면 그냥 메인 렌더링
    return render(request, "main.html")

# 회원 가입
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        try:
            user = UserService.signup(form)
            return redirect("accounts:login")
        except ValidationError as e:
            return render(request, "signup.html", {"form": form, "error": str(e)})
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

            
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = UserService.login(request, email, password)
            return redirect('accounts:main')  # 로그인 성공 후 홈으로
        except ValidationError as e:
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