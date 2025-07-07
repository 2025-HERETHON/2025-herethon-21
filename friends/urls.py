from django.urls import path
from .views import read_friends_list, create_send_friends, read_send_list, create_accept_friend

app_name = 'friends'

urlpatterns = [
    path('list/', read_friends_list, name="read_friends_list"),
    path('send/', create_send_friends, name="create_send_friends"),
    path('received/', read_send_list, name="read_send_list"),
    path('accept/<str:username>/', create_accept_friend, name="create_accept_friend")
]