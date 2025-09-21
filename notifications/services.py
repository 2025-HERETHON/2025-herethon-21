from django.db.models import Case, When, Value, Q, BooleanField, CharField
from django.http import HttpRequest
from django.utils import timezone
from utils.choices import NotificationCategoryType
from utils.validators import validate_auth, validate_not_self
from .models import Notification

class NotificationService:
    def __init__(self, request:HttpRequest):
        self.request = request

    @validate_auth
    def get_list(self):
        notifications = Notification.objects.filter(
            Q(receiver=self.request.user) |  # 받은 알림은 모두 포함
            Q(
                Q(sender=self.request.user) & ~Q(category__in=[
                    NotificationCategoryType.REQUEST.value,
                    NotificationCategoryType.PROD.value
                ])
            )
        ).select_related('sender', 'receiver').annotate(
            category_display=Case(
                When(category=NotificationCategoryType.REQUEST.value, then=Value(NotificationCategoryType.REQUEST.label)),
                When(category=NotificationCategoryType.ACCEPT.value, then=Value(NotificationCategoryType.ACCEPT.label)),
                When(category=NotificationCategoryType.REJECT.value, then=Value(NotificationCategoryType.REJECT.label)),
                When(category=NotificationCategoryType.REACTION.value, then=Value(NotificationCategoryType.REACTION.label)),
                When(category=NotificationCategoryType.PROD.value, then=Value(NotificationCategoryType.PROD.label)),
                output_field=CharField(),
            ),
            is_received=Case(
                When(receiver=self.request.user, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        ).values(
            'id','created_at','sender__nickname','receiver__nickname','category_display','is_received'
        )

        return [
            {
                'id': n['id'],
                'created_at': n['created_at'],
                'content': (
                    f"{n['sender__nickname']}(이)가 {n['category_display']}" 
                    if n['is_received'] 
                    else f"{n['receiver__nickname']}의 {n['category_display']}"
                )
            }
            for n in notifications
        ]

    @validate_auth
    def get_is_prodded(self, friend_id):
        is_prodded = Notification.objects.filter(
            created_at__date=timezone.now().date(),
            sender=self.request.user,
            receiver__id=friend_id,
            category=NotificationCategoryType.PROD,
        ).exists()
        return is_prodded

    @validate_not_self
    @validate_auth
    def post(self, sender, receiver, category:NotificationCategoryType):
        Notification.objects.create(
            sender=sender,
            receiver=receiver,
            category=category # Enum 값이 자동으로 정수로 변환됨
        )

    @validate_auth
    def delete(self, notification:Notification):
        notification.delete()
