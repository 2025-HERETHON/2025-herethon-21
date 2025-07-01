# KakaoAPI/views.py

from django.shortcuts import render, redirect
from .forms import SignupForm
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            return render(request, 'main.html', {'user':user})

    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})



def login(request):
    # POST 요청일 경우 로그인 처리
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return render(request, 'main.html', {'user':user})  # 로그인 성공 시 메인 페이지로 이동
        else:
            return render(request, 'login.html', {
                'error': '아이디 또는 비밀번호가 잘못되었습니다.',
            })

    # GET 요청일 경우 로그인 페이지 렌더링
    return render(request, 'login.html')
    

def logout(request):
    auth_logout(request)
    return redirect('KakaoAPI:login')