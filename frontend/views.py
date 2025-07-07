from django.shortcuts import render, redirect
from django.urls import reverse
import json

def routineingpage(request):
    data_list = [
        {
            "id": 1,
            "content": "준비 스트레칭",
            "details": [
                "텍스트1",
                "텍스트2", 
                "텍스트3"
                ],
            "time": 1, #타이머 테스트용으로 짧게 1분으로 설정해뒀습니다
            "detail_images": [
                "assets/img/fitnessdog.png",
                "assets/img/squat_1.png",
                "assets/img/happy_pipi_hugging.png",
                ],
            "category" : "준비 운동",
            "difficulty" : 2,
        },
        {
            "id": 2,
            "content": "스쿼트",
            "details": [
                "텍스트1",
                "텍스트2", 
                "텍스트3"
                ],
            "time": 5,
            "detail_images": [
                "assets/img/squat_1.png",
                "assets/img/fitnessdog.png",
                "assets/img/happy_pipi_hugging.png",
                ],
            "category" : "하체 근력",
            "difficulty" : 4,
        },
        {
            "id": 3,
            "content": "플랭크",
            "details": [
                "텍스트1",
                "텍스트2", 
                "텍스트3"
                ],
            "time": 3,
            "detail_images": [
                "assets/img/fitnessdog.png",
                "assets/img/squat_1.png",
                "assets/img/happy_pipi_hugging.png",
                ],
            "category" : "코어 근력",
            "difficulty" : 4,
        },
        {
            "id": 4,
            "content": "암서클",
            "details": [
                "텍스트1",
                "텍스트2", 
                "텍스트3"
                ],
            "time": 5,
            "detail_images": [
                "assets/img/fitnessdog.png",
                "assets/img/squat_1.png",
                "assets/img/happy_pipi_hugging.png",
                ],
            "category" : "팔 근력",
            "difficulty" : 3,
        },
        {
            "id": 5,
            "content": "마무리 스트레칭",
            "details": [
                "텍스트1",
                "텍스트2", 
                "텍스트3"
                ],
            "time": 4,
            "detail_images": [
                "assets/img/fitnessdog.png",
                "assets/img/squat_1.png",
                "assets/img/happy_pipi_hugging.png",
                ],
            "category" : "마무리 운동",
            "difficulty" : 2,
        },
    ]
    return render(request,
                    "pages/routine_ing_page.html",
                    {
                        'data_list': data_list,
                        'data_list_json':json.dumps(data_list),
                    }
                ) 

def componentpage(request):
    return render(request,"pages/component_page.html")

def cyclepage(request):
    return render(request,"pages/cycle_page.html")

def scrappage(request):
    return render(request,"pages/scrap_page.html")

def periodpage(request):
    return render(request,"pages/period_page.html")
    return render(request,"pages/component_page.html")

def componentcalendar(request):
    return render(request,"pages/component_calendar.html")
    return render(request,"pages/component_calendar.html")

def mypage(request):
    return render(request,"pages/mypage.html")
    return render(request,"pages/mypage.html")

def onboarding_1(request):
    return render(request, "pages/onboarding_pages/onboarding_1.html")

def onboarding_2(request):
    return render(request, "pages/onboarding_pages/onboarding_2.html")

def onboarding_3(request):
    return render(request, "pages/onboarding_pages/onboarding_3.html")

def signuppage(request):
    return render(request, "pages/onboarding_pages/signup_page.html")

def loginpage(request): #아래 더미데이터는 GPT에게 요청해 받았습니다
    dummy_users = {
        'fitforme@example.com': 'abc123!@#',
    }

    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')

        if email and password:
            if email in dummy_users and dummy_users[email] == password:
                return redirect(reverse('frontend:onboarding_3'))
            else:
                return render(request, 'pages/onboarding_pages/login_page.html', {
                    'error': '정보가 없습니다'
                })

    return render(request, 'pages/onboarding_pages/login_page.html')

def lastmenstruationpage(request):
    return render(request, "pages/onboarding_pages/last_menstruation_page.html")

def purposepage(request):
    return render(request, "pages/onboarding_pages/purpose_page.html")
