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

    return render(request, 'test.html', {
        'menstruations': menstruations,
        'menstruation_average': menstruation_average,
        'menstruation_cycle': menstruation_cycle,
    })

@require_POST
def create_menstruation(request:HttpRequest):
    service = MenstruationService(request)
    message = service.post()
    return redirect('menstruations:root')

@require_POST
def update_menstruation(request:HttpRequest, pk:int):
    service = MenstruationService(request, pk)
    message = service.put()
    return redirect('menstruations:root')

@require_POST
def delete_menstruation(request:HttpRequest, pk:int):
    service = MenstruationService(request, pk)
    message = service.delete()
    return redirect('menstruations:root')