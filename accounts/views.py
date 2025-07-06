from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .services import UserService
from .forms import CustomUserCreationForm
from utils.choices import ExerciseGoalType
from .models import CustomUser

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
            goal_labels = [ExerciseGoalType(int(goal)).label for goal in user.exercise_goal]

            context = {
                'user':user,
                'goal_labels':goal_labels
            }
            
            return render(request, 'main.html', context)
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
    
