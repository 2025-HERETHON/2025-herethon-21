from ast import literal_eval
from datetime import timedelta
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.utils.dateparse import parse_duration
from django.views.decorators.http import require_GET, require_POST
from utils.choices import NotificationCategoryType
from utils.constants import CACHE_KEY
from notifications.services import NotificationService
from .models import ExerciseHistory
from .services import ExerciseAiService, ScrappedExerciseRoutineService, ExerciseHistoryService, ExerciseReviewService, ReactedExerciseReviewService

@require_GET
def test(request:HttpRequest):
    ai_service = ExerciseAiService(request)
    ai_exercise_routines = ai_service.get()

    scrap_service = ScrappedExerciseRoutineService(request)
    scrapped_exercise_routines = scrap_service.get_list()

    history_service = ExerciseHistoryService(request)
    exercise_histories = history_service.get_list()

    review_service = ExerciseReviewService(request)
    exercise_reviews = review_service.get_list()

    return render(request, 'test_exercises.html', {
        'ai_exercise_routines': ai_exercise_routines,
        'scrapped_exercise_routines': scrapped_exercise_routines,
        'exercise_histories': exercise_histories,
        'exercise_reviews': exercise_reviews,
    })

def test_exercise_start(request:HttpRequest): # 운동방 페이지
    exercise_routine_str = request.POST.get('exercise_routine')
    exercise_routine:list[dict[str,any]] = literal_eval(exercise_routine_str)
    exercise_routine_duration = sum((parse_duration(item['exercise']['duration']) for item in exercise_routine), timedelta(0))
    
    service = ExerciseHistoryService(request)
    exercise_history_id, message = service.post(exercise_routine_duration)

    cache.set(CACHE_KEY(request.user.username).EXERCISE_ROUTINE, exercise_routine, timeout=3600*2)
    cache.set(CACHE_KEY(request.user.username).EXERCISE_HISTORY_ID, exercise_history_id, timeout=3600*2)

    return render(request, 'test_exercise_start.html', {
        'exercise_routine': exercise_routine,
    })

def test_exercise_end(request:HttpRequest): # 운동 후 운동 리뷰 작성 페이지
    exercise_routine = cache.get(CACHE_KEY(request.user.username).EXERCISE_ROUTINE)
    exercise_history_id = cache.get(CACHE_KEY(request.user.username).EXERCISE_HISTORY_ID)

    return render(request, 'test_exercise_end.html', {
        'exercise_routine': exercise_routine,
        'exercise_history_id': exercise_history_id,
    })

@require_POST
def create_scrapped_exercise_routine(request:HttpRequest):
    service = ScrappedExerciseRoutineService(request)
    message = service.post()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def delete_scrapped_exercise_routine(request:HttpRequest, scrapped_at:str):
    service = ScrappedExerciseRoutineService(request)
    message = service.delete(scrapped_at)
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def create_exercise_history(request:HttpRequest):
    service = ExerciseHistoryService(request)
    message = service.post()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def create_exercise_review(request:HttpRequest):
    service = ExerciseReviewService(request)
    message = service.post()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def update_exercise_review(request:HttpRequest, pk:int):
    service = ExerciseReviewService(request, pk)
    message = service.put()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def delete_exercise_review(request:HttpRequest, pk:int):
    service = ExerciseReviewService(request, pk)
    message = service.delete()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def createordelete_reacted_exercise_review(request:HttpRequest, exercise_review_id:int):
    service = ReactedExerciseReviewService(request)
    message = service.post(exercise_review_id)

    if '추가' in message:
        exercise_history = ExerciseHistory.objects.get(exercise_review__id=exercise_review_id)

        service = NotificationService(request)
        service.post(
            sender=request.user,
            receiver=exercise_history.user,
            category=NotificationCategoryType.REACTION
        )

    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))