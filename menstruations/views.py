from django.shortcuts import render, redirect
from django.http import HttpRequest
from .services import MenstruationService

def root(request:HttpRequest):
    month_str = request.GET.get('month')

    service = MenstruationService(request)
    response_list = service.get_list()
    response_average = service.get_average()
    response_cycle = service.get_cycle(month_str)

    if (response_list['status'] == 200) and (response_average['status'] == 200) and (response_cycle['status'] == 200):
        return render(request, 'test.html', {
            'menstruation_list': response_list['data'],
            'menstruation_average': response_average['data'],
            'menstruation_cycle': response_cycle['data'],
        })

def create_menstruation(request:HttpRequest):
    if request.method == 'POST':
        service = MenstruationService(request)
        response = service.post()
        if response['status'] == 201:
            return redirect('menstruations:root')
    return render(request, 'create_menstruation.html')

def update_menstruation(request:HttpRequest, pk:int):
    if request.method == 'POST':
        service = MenstruationService(request, pk)
        response = service.put()
        if response['status'] == 204:
            return redirect('menstruations:root')

def delete_menstruation(request:HttpRequest, pk:int):
    if request.method == 'POST':
        service = MenstruationService(request, pk)
        response = service.delete()
        if response['status'] == 204:
            return redirect('menstruations:root')