from django.http import HttpRequest
from django.utils import timezone
from utils.choices import NotificationCategoryType
from utils.validators import validate_auth, validate_not_self
from accounts.models import CustomUser
from .models import Notification

class NotificationService:
    def __init__(self, request:HttpRequest):
        self.request = request

    @validate_auth
    def get_list(self):
        notifications = Notification.objects.filter(
            receiver=self.request.user,
        ).values(
            'id','created_at','sender__nickname','category'
        )
        return notifications

    @validate_auth
    def get_is_prodded(self, friend_username):
        is_prodded = Notification.objects.filter(
            created_at__date=timezone.now(),
            sender=self.request.user,
            receiver__username=friend_username,
            category=NotificationCategoryType.PROD,
        ).exists()
        return is_prodded

    @validate_not_self
    @validate_auth
    def post(self, sender:CustomUser, receiver:CustomUser, category:NotificationCategoryType):
        Notification.objects.create(
            sender=sender,
            receiver=receiver,
            category=category # Enum 값이 자동으로 정수로 변환됨
        )
        return '알림을 추가했습니다.'