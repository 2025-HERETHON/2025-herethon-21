from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('example', example, name='example'),
    path("componentpage", componentpage, name="componentpage"),
    path("routineingpage", routineingpage, name="routineingpage"),
]