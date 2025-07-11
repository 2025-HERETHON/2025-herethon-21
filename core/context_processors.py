from django.http import HttpRequest
from exercises.services import ExerciseReviewService
from menstruations.services import MenstruationService

def global_components(request:HttpRequest):
    """모든 템플릿에서 사용할 전역 컨텍스트"""

    context = {}

    menstruation_service = MenstruationService(request)
    menstruation_cycle = menstruation_service.get_cycle()

    exercise_review_service = ExerciseReviewService(request)
    exercise_reviews = exercise_review_service.get_list()

    # 로그인한 사용자에게만 제공
    if request.user.is_authenticated:
        context.update({
            'menstruation_cycle': menstruation_cycle,
            'exercise_reviews': exercise_reviews,
        })

    return context