from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from utils.choices import NotificationCategoryType
from accounts.models import CustomUser
from .services import NotificationService

@require_GET
def read_is_prodded(request:HttpRequest, friend_username:str):
    service = NotificationService(request)
    notification_list = service.get_list()
    is_prodded = service.get_is_prodded(friend_username)

    return render(request, 'test.html', {
        'friend_username': friend_username,
        'notification_list': notification_list,
        'is_prodded': is_prodded,
    })

@require_POST
def create_notification(request:HttpRequest):
    service = NotificationService(request)

    receiver_str = request.POST.get('receiver')
    category_str = request.POST.get('category')
    receiver = get_object_or_404(CustomUser, username=receiver_str)
    category = NotificationCategoryType(int(category_str))

    message = service.post(request.user, receiver, category)

    return redirect(request.META.get('HTTP_REFERER', '/'))