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

def restpage(request):
    return render(request,"pages/rest_page.html")

def periodpage(request):
    return render(request,"pages/period_page.html")
    return render(request,"pages/component_page.html")

def componentcalendar(request):
    return render(request,"pages/component_calendar.html")
    return render(request,"pages/component_calendar.html")

def mypage(request):
    return render(request,"pages/mypage.html")

def friendpage(request):
    return render(request,"pages/friend_page.html")


def onboarding_1(request):
    return render(request, "pages/onboarding_pages/onboarding_1.html")

def onboarding_2(request):
    return render(request, "pages/onboarding_pages/onboarding_2.html")

def onboarding_3(request):
    return render(request, "pages/onboarding_pages/onboarding_3.html")

def signuppage(request):
    return render(request, "pages/onboarding_pages/signup_page.html")

def loginpage(request): #아래 더미데이터는 GPT에게 받은 임시 데이터입니다
    dummy_users = {
        'fitforme@example.com': 'abc123!@#',
    }

    context = {}

    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')

        if email or password:
            import re
            # 이메일 형식 검증
            email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(email_regex, email or ''):
                context['email_error'] = '이메일 형식이 잘못되었습니다.'

            elif email in dummy_users:
                if dummy_users[email] == password:
                    return redirect(reverse('frontend:onboarding_3'))
                else:
                    context['password_error'] = '비밀번호가 틀렸습니다.'
            else:
                context['password_error'] = '비밀번호가 틀렸습니다.'

            context['email'] = email
            context['password'] = password

    return render(request, 'pages/onboarding_pages/login_page.html', context)

def lastmenstruationpage(request):
    return render(request, "pages/onboarding_pages/last_menstruation_page.html")

def purposepage(request):
    return render(request, "pages/onboarding_pages/purpose_page.html")

def alarmpage(request):
    return render(request, "pages/alarm_page.html")

def mypagemain(request):
    data_list = [
        {
            "id": 1,
            "start_time": "07:00",
            "end_time": "08:00",
            "duration_minutes": 60,
            "content": "아 오늘 운동 힘들었다",
            "emotion_counts": {
                "crying": 5,
                "anger": 2,
                "agree": 10,
                "surprized": 1,
                "smile": 0
            },
        },
        {
            "id": 2,
            "start_time": "20:00",
            "end_time": "20:40",
            "duration_minutes": 40,
            "content": "ㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴ",
            "emotion_counts": {
                "crying": 3,
                "anger": 0,
                "agree": 7,
                "surprized": 9,
                "smile": 1
            },
        },
    ]
    return render(request, "pages/mypage_main.html", {"data_list": data_list})

def makefriends(request):
    data_list = [
        {
            "id": 1,
            "name": "성혜린",
            "email": "hyerin@gmail.com",
            "profile_photo" : "assets/img/anger.png",
        },
        {
            "id": 2,
            "name": "이승언",
            "email": "seungun@hanmail.com",
            "profile_photo" : "assets/img/smile.png",
        },
        {
            "id": 3,
            "name": "백수진",
            "email": "sujin@naver.com",
            "profile_photo" : "assets/img/surprized.png",
        },
        {
            "id": 4,
            "name": "김시원",
            "email": "siwon@gmail.com",
            "profile_photo" : "assets/img/agree.png",
        },
        {
            "id": 5,
            "name": "허윤아",
            "email": "yuna@gmail.com",
            "profile_photo" : "assets/img/crying.png",
        },
    ]
    return render(request, "pages/make_friends_pages/friends_email_input.html", {"data_list": data_list})

def friendsconfirm(request):
    return render(request, "pages/make_friends_pages/friends_confirm.html")

def friended(request):
    return render(request, "pages/make_friends_pages/friended.html")
