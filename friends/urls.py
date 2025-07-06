from django.urls import path
from .views import read_friends_list, create_send_friends

app_name = 'friends'

urlpatterns = [
    path('list/', read_friends_list, name="read_friends_list"),
    path('send/', create_send_friends, name="create_send_friends"),
]