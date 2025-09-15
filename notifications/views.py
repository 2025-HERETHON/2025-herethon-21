from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest
from django.views.decorators.http import require_POST
from utils.choices import NotificationCategoryType
from accounts.models import CustomUser
from .services import NotificationService

@require_POST
def create_notification(request:HttpRequest):
    service = NotificationService(request)

    receiver_str = request.POST.get('receiver')
    category_str = request.POST.get('category')
    receiver = get_object_or_404(CustomUser, id=receiver_str)
    category = NotificationCategoryType(int(category_str))

    message = service.post(request.user, receiver, category)

    return redirect(request.META.get('HTTP_REFERER', '/'))
