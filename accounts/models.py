import nanoid
from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.choices import ExerciseGoalType
from utils.json_handlers import JSONIntChoicesListHandler
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    # AbstractUser 모델 오버라이딩
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(
        unique=True,
        error_messages={'unique': '이미 존재하는 이메일입니다.',},
    )
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # 커스텀 필드
    id = models.CharField(
        max_length=21,
        unique=True,
        editable=False,
    )
    nickname = models.CharField(
        max_length=100,
        blank=True,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    profile_image = models.ImageField(
        upload_to='user/profile_image',
        default='user/profile_image/default.jpg',
        null=True,
        blank=True,
    )
    exercise_goal = models.JSONField(
        default=list, # list[int]
        null=True,
        blank=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercise_goal_handler = JSONIntChoicesListHandler(
            self,
            'exercise_goal',
            ExerciseGoalType,
        )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if (not self.pk) and (not self.id):
            self.id = nanoid.generate()
        super().save(*args, **kwargs)
