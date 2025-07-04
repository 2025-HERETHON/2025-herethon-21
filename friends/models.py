from django.db import models
from utils.choices import StatusType
from accounts.models import CustomUser

class Friend(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    sender = models.ForeignKey(
        CustomUser,
        related_name='friend_sendings',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        CustomUser,
        related_name='friend_receivings',
        on_delete=models.CASCADE,
    )
    status = models.PositiveSmallIntegerField(
        choices=StatusType.choices,
        default=1,
    )

    def __str__(self):
        return f'{self.sender.email} → {self.receiver.email}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['sender','receiver'],
                name='친구 요청은 한 번만 합니다.',
            )
        ]