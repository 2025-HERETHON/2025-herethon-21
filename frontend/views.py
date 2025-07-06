from django.shortcuts import render
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
            "image": "assets/img/fitnessdog.png", 
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
            "image": "assets/img/fitnessdog.png", 
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
            "image": "assets/img/fitnessdog.png", 
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
            "image": "assets/img/fitnessdog.png", 
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
            "image": "assets/img/fitnessdog.png", 
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

def componentcalendar(request):
    return render(request,"pages/component_calendar.html")

def mypage(request):
    return render(request,"pages/mypage.html")

def onboarding_1(request):
    return render(request, "pages/onboarding_pages/onboarding_1.html")

def onboarding_2(request):
    return render(request, "pages/onboarding_pages/onboarding_2.html")

def onboarding_3(request):
    return render(request, "pages/onboarding_pages/onboarding_3.html")

def signuppage(request):
    return render(request, "pages/onboarding_pages/signup_page.html")

def loginpage(request):
    return render(request, "pages/onboarding_pages/login_page.html")

def lastmenstruationpage(request):
    return render(request, "pages/onboarding_pages/last_menstruation_page.html")

def preferencepage(request):
    return render(request, "pages/onboarding_pages/preference_page.html")

def purposepage(request):
    return render(request, "pages/onboarding_pages/purpose_page.html")
