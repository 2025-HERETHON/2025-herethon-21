from django.urls import path
from .views import *

app_name = 'notifications'

urlpatterns = [
    path('create', create_notification, name='create_notification'),
    path('read/<str:friend_username>', read_is_prodded, name='read_is_prodded'),
]