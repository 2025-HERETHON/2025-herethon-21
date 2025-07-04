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
