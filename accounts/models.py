from string import ascii_lowercase, digits
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_nanoid.models import NANOIDField
from utils.choices import ExerciseGoalType
from utils.json_handlers import JSONIntChoicesListHandler
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    # AbstractUser 모델 오버라이딩
    username = NANOIDField(
        editable=False,
        secure_generated=True,
        alphabetically=ascii_lowercase+digits,
        size=16,
    )
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
    nickname = models.CharField(
        max_length=10,
    )
    exercise_goal = models.JSONField(
        default=list, # list[int]
    )
    profile_image = models.ImageField(
        upload_to='user/profile_image',
        null=True,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
        default="",
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