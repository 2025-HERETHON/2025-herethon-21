from django.urls import path
from .views import *

app_name = 'notifications'

urlpatterns = [
    path('create', create_notification, name='create'),
]