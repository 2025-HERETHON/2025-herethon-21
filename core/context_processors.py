from django.http import HttpRequest
from menstruations.services import MenstruationService

def global_components(request:HttpRequest):
    """모든 템플릿에서 사용할 전역 컨텍스트"""
    
    context = {}

    service = MenstruationService(request)
    menstruation_cycle = service.get_cycle()
    
    # 로그인한 사용자에게만 제공
    if request.user.is_authenticated:
        context.update({
            'menstruation_cycle': menstruation_cycle,
        })
    
    return context