from django.urls import path
from .views import read_friends_list, create_send_friends, read_receive_list, create_accept_friend, create_reject_friend, read_friend_detail

app_name = 'friends'

urlpatterns = [
    path('list/', read_friends_list, name="read_friends_list"),
    path('send/', create_send_friends, name="create_send_friends"),
    path('received/', read_receive_list, name="read_send_list"),
    path('accept/<str:id>/', create_accept_friend, name="create_accept_friend"),
    path('reject/<str:id>/', create_reject_friend, name="create_reject_friend"),
    path('detail/<str:id>/', read_friend_detail, name="read_friend_detail"),  
]
