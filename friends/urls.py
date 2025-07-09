from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import read_friends_list, create_send_friends, read_send_list, create_accept_friend, create_reject_friend, read_friend_detail

app_name = 'friends'

urlpatterns = [
    path('list/', read_friends_list, name="read_friends_list"),
    path('send/', create_send_friends, name="create_send_friends"),
    path('received/', read_send_list, name="read_send_list"),
    path('accept/<str:username>/', create_accept_friend, name="create_accept_friend"),
    path('reject/<str:username>/', create_reject_friend, name="create_reject_friend"),
    path('detail/<str:username>/', read_friend_detail, name="read_friend_detail"),  

]
