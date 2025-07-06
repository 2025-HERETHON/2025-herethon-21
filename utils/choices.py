from django.db.models import IntegerChoices

class ExerciseGoalType(IntegerChoices):
    FIGURE = 1, '체형 관리'
    HEALTH = 2, '건강 관리'
    STRESS = 3, '스트레스 해소'
    MUSCLE = 4, '근력 강화'
    FLEXIBILITY = 5, '유연성 향상'

class ExerciseCategoryType(IntegerChoices):
    FULL = 1, '전신'
    UPPER = 2, '상체'
    LOWER = 3, '하체'
    CORE = 4, '코어'

class ReactionEmojiType(IntegerChoices):
    SAD = 1, '😣'
    ANGRY = 2, '😑'
    CLOSE = 3, '😌'
    OPEN = 4, '😶'
    SMILE = 5, '😊'

class FriendStatusType(IntegerChoices):
    PENDING = 1, '대기'
    ACCEPT = 2, '수락'
    REJECT = 3, '거절'

class NotificationCategoryType(IntegerChoices):
    REQUEST = 1, '친구 요청'
    ACCEPT = 2, '친구 요청을 수락'
    REJECT = 3, '친구 요청을 거절'
    REACTION = 4, '운동 리뷰에 반응'
    PROD = 5, '콕 찌르기'