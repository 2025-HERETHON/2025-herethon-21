from django.db import models
from accounts.models import CustomUser

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
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.user.email}: {self.date}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','date'],
                name='사용자는 컨디션 리뷰를 하루에 한 번만 작성합니다.',
            )
        ]