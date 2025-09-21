from ast import literal_eval
from datetime import date, timedelta
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.dateparse import parse_duration
from django.utils.timezone import now as timezone_now
from utils.choices import ReactionEmojiType, ExerciseGoalType
from utils.constants import CACHE_KEY
from utils.json_handlers import JSONIntChoicesListHandler
from conditionreviews.models import ConditionReview
from exercises.services import ExerciseAiService, ScrappedExerciseRoutineService, ExerciseHistoryService, ExerciseReviewService
from menstruations.services import MenstruationService
from notifications.services import NotificationService

CustomUser = get_user_model()

def routineingpage(request:HttpRequest):
    exercise_routine_str = request.POST.get('exercise_routine')
    exercise_routine:list[dict[str,any]] = literal_eval(exercise_routine_str)
    exercise_routine_duration = sum((parse_duration(item['exercise']['duration']) for item in exercise_routine), timedelta(0))
    
    service = ExerciseHistoryService(request)
    exercise_history_id, message = service.post(exercise_routine_duration)

    cache.set(CACHE_KEY(request.user.id).EXERCISE_ROUTINE, exercise_routine, timeout=3600*2)
    cache.set(CACHE_KEY(request.user.id).EXERCISE_HISTORY_ID, exercise_history_id, timeout=3600*2)

    return render(request, 'pages/routine_ing_page.html', {
        'exercise_routine': exercise_routine,
    })

def cyclepage(request:HttpRequest):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()

    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()
    today_phase = menstruation_service.get_today_phase()

    ai_service = ExerciseAiService(request)
    ai_exercise_routines = ai_service.get()

    return render(request,"pages/cycle_page.html", {
        'exercise_reviews': exercise_reviews,
        'menstruation_cycle': menstruation_cycle,
        "today_phase": today_phase,
        'ai_exercise_routines': ai_exercise_routines,
    })

def scrappage(request:HttpRequest):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()
    
    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()

    scrap_service = ScrappedExerciseRoutineService(request)
    scrapped_exercise_routines = scrap_service.get_list()

    return render(request,"pages/scrap_page.html", {
        'exercise_reviews': exercise_reviews,
        'menstruation_cycle': menstruation_cycle,
        'scrapped_exercise_routines': scrapped_exercise_routines,
    })

def restpage(request:HttpRequest):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()
    
    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()

    return render(request,"pages/rest_page.html", {
        'exercise_reviews': exercise_reviews,
        'menstruation_cycle': menstruation_cycle,
    })

def periodpage(request:HttpRequest):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()

    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()
    menstruations = menstruation_service.get_list()
    menstruation_average = menstruation_service.get_average()
    
    return render(request, "pages/period_page.html", {
        'exercise_reviews': exercise_reviews,
        'menstruation_cycle': menstruation_cycle,
        'menstruations': menstruations,
        'menstruation_average': menstruation_average,
    })

def onboarding_1(request:HttpRequest):
    return render(request, "pages/onboarding_pages/onboarding_1.html")

def onboarding_2(request:HttpRequest):
    return render(request, "pages/onboarding_pages/onboarding_2.html")

def onboarding_3(request:HttpRequest):
    return render(request, "pages/onboarding_pages/onboarding_3.html")

def signuppage(request:HttpRequest):
    return render(request, "pages/onboarding_pages/signup_page.html")

def loginpage(request:HttpRequest): #아래 더미데이터는 GPT에게 받은 임시 데이터입니다
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
                    return redirect(reverse('frontend:cyclepage'))
                else:
                    context['password_error'] = '비밀번호가 틀렸습니다.'
            else:
                context['password_error'] = '비밀번호가 틀렸습니다.'

            context['email'] = email
            context['password'] = password

    return render(request, 'pages/onboarding_pages/login_page.html', context)

def lastmenstruationpage(request:HttpRequest):
    return render(request, "pages/onboarding_pages/last_menstruation_page.html")

def purposepage(request:HttpRequest):
    return render(request, "pages/onboarding_pages/purpose_page.html")

def alarmpage(request:HttpRequest):
    service = NotificationService(request)
    notification_list = service.get_list()
    
    return render(request, "pages/alarm_page.html", {
        'notification_list': notification_list,
    })

def mypagemain(request:HttpRequest):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()
    
    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()

    history_service = ExerciseHistoryService(request)
    exercise_histories = history_service.get_list()

    # 운동 목표 변환
    goal_labels = []
    if request.user.is_authenticated:
        goals = request.user.exercise_goal  # 예: ["1", "2", "4"]
        goal_labels = [ExerciseGoalType(int(g)).label for g in goals]

    # 컨디션 리뷰 조회용 context
    today = date.today()
    now_time = timezone_now().strftime("%H:%M")
    review = ConditionReview.objects.filter(user=request.user, date=today).first()
    review_time = review.updated_at.strftime("%H:%M") if review else None

    return render(request, "pages/mypage_main.html", {
        'exercise_reviews': exercise_reviews,
        'menstruation_cycle': menstruation_cycle,
        "exercise_histories": exercise_histories,
        "goal_labels": goal_labels,
        "today": today,
        "now": now_time,
        "review": review,
        "rating_choices": ReactionEmojiType.choices,
        "rating": getattr(review, "rating", None),
        "review_time":review_time
    })

def makefriends(request:HttpRequest):
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

def friendsconfirm(request, email):
    receiver_user = get_object_or_404(CustomUser, email=email)
    return render(request, 'pages/make_friends_pages/friends_confirm.html', {
        'receiver_user': receiver_user
    })
def friended(request):
    sender = request.user
    receiver_email = request.GET.get("email")  # 또는 request.POST.get 등
    receiver = get_object_or_404(CustomUser, email=receiver_email)

    return render(request, "pages/make_friends_pages/friended.html", {
        "sender": sender,
        "receiver": receiver,
        "receiver_email": receiver_email
    })

def finishedroutine(request:HttpRequest):
    exercise_routine = cache.get(CACHE_KEY(request.user.id).EXERCISE_ROUTINE)
    exercise_history_id = cache.get(CACHE_KEY(request.user.id).EXERCISE_HISTORY_ID)
    
    return render(request, "pages/finished_routine.html", {
        'exercise_routine': exercise_routine,
        'exercise_history_id': exercise_history_id,
    })

def editpage(request:HttpRequest):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()

    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()

    user = request.user
    handler = JSONIntChoicesListHandler(user, "exercise_goal", ExerciseGoalType)

    return render(request, 'pages/edit_page.html', {
        'menstruation_cycle': menstruation_cycle,
        'exercise_reviews': exercise_reviews,
        'user': user,
        'goal_choices': ExerciseGoalType.choices,
        'selected_goals': handler.get_int_values(),
    })

def friendpage(request:HttpRequest, friend_id:str):
    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()
    
    notification_service = NotificationService(request)
    is_prodded = notification_service.get_is_prodded(friend_id)

    return render(request, "pages/friend_page.html", {
        'exercise_reviews': exercise_reviews,
        'friend_id': friend_id,
        'is_prodded': is_prodded,
    })


def base_side(request):
    return render(request, "example/base_side.html")
def base_side_right(request):
    return render(request, "example/base_side_right.html")
def base_side_left(request):
    return render(request, "example/base_side_left.html")
def willbedeleted(request):
    return render(request, "example/will_bedeleted.html")
