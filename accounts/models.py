from string import ascii_lowercase, digits
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_nanoid.models import NANOIDField
from utils.mixins import JSONIntListHandler, JSONIntChoicesListHandler
from utils.choices import ExerciseGoalType
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
    exercise_preference = models.JSONField(
        default=list, # list[int]
    )
    exercise_goal = models.JSONField(
        default=list, # list[int]
    )
    profile_image = models.ImageField(
        upload_to='user/image/profile',
        null=True,
        blank=True,
    )
    background_image = models.ImageField(
        upload_to='user/image/background',
        null=True,
        blank=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercise_preference_handler = JSONIntListHandler(
            self,
            'exercise_preference',
        )
        self.exercise_goal_handler = JSONIntChoicesListHandler(
            self,
            'exercise_goal',
            ExerciseGoalType,
        )