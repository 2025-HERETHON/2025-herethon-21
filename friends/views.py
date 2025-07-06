from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.choices import FriendStatusType
from django.db.models import Q
from .models import Friends

@login_required
def read_friends_list(request):
    user = request.user
    friends = Friends.objects.filter(
        Q(sender=user) | Q(receiver=user),
        status=FriendStatusType.ACCEPT
    )
    return render(request, "friend_list.html", {"friends":friends})

# urlpatterns = [
#     path('list/', read_friends_list, name="read_friends_list"),
#     path('send/', create_send_friends, name="create_send_friends"),
#     path('received/', read_send_list, name="read_send_list"),
#     path('accept/<str:username>', create_accept_friend, name="create_accept_friend"),
#     path('reject/<str:username>', create_reject_friend, name="create_reject_friend")
# ]