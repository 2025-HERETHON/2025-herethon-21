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
    data_list = [
        {
            "date": "2025-05-09",
            "time": "13:02",
            "duration": "20분",
            "routines": [
                {"id": 1, "name": "준비 스트레칭", "duration": "3분", "part": "몸풀기"},
                {"id": 2, "name": "런지", "duration": "5분", "part": "하체 근력"},
                {"id": 3, "name": "버피 테스트", "duration": "3분", "part": "전신 유산소"},
                {"id": 4, "name": "팔 돌리기", "duration": "5분", "part": "어깨 유연성"},
                {"id": 5, "name": "마무리 스트레칭", "duration": "4분", "part": "근육 이완"},
            ]
        },
        {
            "date": "2025-05-09",
            "time": "09:10",
            "duration": "20분",
            "routines": [
                {"id": 1, "name": "워밍업 점핑잭", "duration": "3분", "part": "전신 워밍업"},
                {"id": 2, "name": "사이드 런지", "duration": "5분", "part": "하체 근력"},
                {"id": 3, "name": "플랭크 트위스트", "duration": "3분", "part": "복근/코어"},
                {"id": 4, "name": "암 레이즈", "duration": "5분", "part": "팔/어깨"},
                {"id": 5, "name": "쿨다운 요가", "duration": "4분", "part": "유연성"},
            ]
        },
        {
            "date": "2025-05-08",
            "time": "18:00",
            "duration": "20분",
            "routines": [
                {"id": 1, "name": "목 스트레칭", "duration": "3분", "part": "경추 이완"},
                {"id": 2, "name": "스쿼트", "duration": "5분", "part": "하체 근력"},
                {"id": 3, "name": "마운틴 클라이머", "duration": "3분", "part": "코어/전신"},
                {"id": 4, "name": "삼두근 킥백", "duration": "5분", "part": "팔/삼두"},
                {"id": 5, "name": "호흡 명상", "duration": "4분", "part": "호흡 안정"},
            ]
        },
    ]
    return render(request,"pages/scrap_page.html", {"data_list": data_list})

def restpage(request):
    return render(request,"pages/rest_page.html")

def periodpage(request):
    dummy_period_data = [
        {
            "start_date": "2025.06.01.",
            "end_date": "2025.06.07.",
            "duration": 7,
            "cycle": 28,
        },
        {
            "start_date": "2025.06.29.",
            "end_date": "2025.07.05.",
            "duration": 7,
            "cycle": 35,
        },
        {
            "start_date": "2025.07.26.",
            "end_date": "2025.08.02.",
            "duration": 8,
            "cycle": 30,
        },
    ]
    context = {
        "period_data": dummy_period_data
    }
    return render(request, "pages/period_page.html", context)
    return render(request,"pages/component_page.html")

def componentcalendar(request):
    return render(request,"pages/component_calendar.html")
    return render(request,"pages/component_calendar.html")

def mypage(request):
    return render(request,"pages/mypage.html")

def friendpage(request):
    data_list = [
        {
            "id": 1,
            "start_time": "08:40",
            "end_time": "09:00",
            "duration_minutes": 20,
            "content": "배고파",
            "rating": 3,
            "emotion_counts": {
                "crying": 0,
                "anger": 0,
                "agree": 9,
                "surprized": 1,
                "smile": 3
            },
        },
        {
            "id": 2,
            "start_time": "18:00",
            "end_time": "19:00",
            "duration_minutes": 60,
            "content": "고양이귀여워",
            "rating": 5,
            "emotion_counts": {
                "crying": 0,
                "anger": 0,
                "agree": 98,
                "surprized": 0,
                "smile":10
            },
        },
    ]

    return render(request,"pages/friend_page.html",{"data_list": data_list})


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
            "rating": 1,
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
            "rating": 4,
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

def finishedroutine(request):
    return render(request, "pages/finished_routine.html")

def editpage(request):
    return render(request,"pages/edit_page.html")
  
