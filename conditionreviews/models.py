from django.db import models
from django.contrib.auth import get_user_model
from utils.choices import ReactionEmojiType

CustomUser = get_user_model()

class ConditionReview(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='condition_reviews',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    rating = models.PositiveSmallIntegerField(
        choices=ReactionEmojiType.choices,
    )
    comment = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'[{self.user.email}] {self.date}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','date'],
                name='unique_user_date',
                violation_error_message='사용자는 컨디션 리뷰를 한 날짜에 한 개만 작성할 수 있습니다.',
            )
        ]
        ordering = ['date']
