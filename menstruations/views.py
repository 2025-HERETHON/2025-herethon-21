from django.shortcuts import render, redirect
from django.http import HttpRequest
from .services import MenstruationService

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

def create_menstruation(request:HttpRequest):
    if request.method == 'POST':
        service = MenstruationService(request)
        message = service.post()
        return redirect('menstruations:root')

def update_menstruation(request:HttpRequest, pk:int):
    if request.method == 'POST':
        service = MenstruationService(request, pk)
        message = service.put()
        return redirect('menstruations:root')

def delete_menstruation(request:HttpRequest, pk:int):
    if request.method == 'POST':
        service = MenstruationService(request, pk)
        message = service.delete()
        return redirect('menstruations:root')