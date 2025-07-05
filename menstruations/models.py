from django.db import models
from accounts.models import CustomUser

class Menstruation(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='menstruations',
        on_delete=models.CASCADE,
    )
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'[{self.user.email}] {self.start} - {self.end}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','start','end'],
                name='unique_user_start_end',
                violation_error_message='사용자는 월경을 같은 기간에 한 번만 할 수 있습니다.',
            )
        ]
        ordering = ['-start']