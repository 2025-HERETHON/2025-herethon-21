from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest
from django.views.decorators.http import require_POST
from utils.choices import NotificationCategoryType
from notifications.services import NotificationService
from .models import ExerciseHistory
from .services import ScrappedExerciseRoutineService, ExerciseHistoryService, ExerciseReviewService, ReactedExerciseReviewService

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
