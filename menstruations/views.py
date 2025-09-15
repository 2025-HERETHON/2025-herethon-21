from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest
from django.views.decorators.http import require_POST
from .services import MenstruationService

@require_POST
def create_menstruation(request:HttpRequest):
    service = MenstruationService(request)
    message = service.post()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def update_menstruation(request:HttpRequest, pk:int):
    service = MenstruationService(request, pk)
    message = service.put()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_POST
def delete_menstruation(request:HttpRequest, pk:int):
    service = MenstruationService(request, pk)
    message = service.delete()
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', '/'))
