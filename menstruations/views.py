from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from .services import MenstruationService

@require_GET
def root(request:HttpRequest):
    service = MenstruationService(request)
    menstruations = service.get_list()
    menstruation_average = service.get_average()
    menstruation_cycle = service.get_cycle()
    today_phase = service.get_today_phase()

    return render(request, 'test.html', {
        'menstruations': menstruations,
        'menstruation_average': menstruation_average,
        'menstruation_cycle': menstruation_cycle,
        'today_phase': today_phase,
    })

@require_GET
def test_create_menstruation(request:HttpRequest):
    return render(request, 'test_create_menstruation.html')

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
