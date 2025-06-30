from django.shortcuts import render, redirect
from .forms import SignupForm
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
            
            return redirect('KakaoAPI:main')
        
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        
        if user:
            auth_login(request, user)
            return render(request, 'main.html', {'username':username})
        else:
            return render(request, 'login.html', {
                'error' : '아이디 또는 비밀번호가 잘못 되었습니다.',
            })
            
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('KakaoAPI:login')