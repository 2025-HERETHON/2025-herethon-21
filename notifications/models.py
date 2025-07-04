from django.db import models
from utils.choices import NotificationCategoryType
from accounts.models import CustomUser

class Notification(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    sender = models.ForeignKey(
        CustomUser,
        related_name='notification_sendings',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        CustomUser,
        related_name='notification_receivings',
        on_delete=models.CASCADE,
    )
    category = models.PositiveSmallIntegerField(
        choices=NotificationCategoryType.choices,
    )

    def __str__(self):
        return f'{self.sender.email}이/가 {self.receiver.email}에게 {NotificationCategoryType(self.category).label}함'