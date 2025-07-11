from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.choices import FriendStatusType
from django.db.models import Q
from .models import Friend
from accounts.models import CustomUser
from .services import FriendService
from notifications.services import NotificationService
from django.contrib import messages
from utils.json_handlers import JSONIntChoicesListHandler
from utils.choices import ExerciseGoalType, NotificationCategoryType


@login_required
def read_friends_list(request):
    user = request.user
    friends = Friend.objects.filter(
        Q(sender=user) | Q(receiver=user),
        status=FriendStatusType.ACCEPT
    )
    return render(request, "friend_list.html", {"friends":friends})

@login_required
def create_send_friends(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            receiver = CustomUser.objects.get(email=email)
            FriendService.send_request(request.user, receiver)
            service = NotificationService(request)
            service.post(
                sender=request.user,
                receiver=receiver,
                category=NotificationCategoryType.REQUEST
            )
            messages.success(request, f"{email}님에게 친구 요청을 보냈습니다.")
        except CustomUser.DoesNotExist:
            messages.error(request, "해당 이메일의 사용자가 존재하지 않습니다.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect("friends:create_send_friends")
    return render(request, "friend_request_send.html")

@login_required
def read_receive_list(request):
    user = request.user
    friend_requests = Friend.objects.filter(
        receiver=user,
        status=FriendStatusType.PENDING
    )
    return render(request, "friend_request_received.html", {"friend_requests":friend_requests})

@login_required
def create_accept_friend(request, username):
    if request.method == "POST":
        friend = Friend.objects.filter(
            receiver=request.user,
            sender__username=username,
            status=FriendStatusType.PENDING
        ).first()
        if friend:
            FriendService.accept_request(friend)
            service = NotificationService(request)
            service.post(                
                sender=friend.sender,
                receiver=friend.receiver,
                category=NotificationCategoryType.ACCEPT
            )
        
        return redirect("friends:read_friends_list")
    
@login_required
def create_reject_friend(request, username):
    if request.method == "POST":
        friend = Friend.objects.filter(
            receiver=request.user,
            sender__username=username,
            status=FriendStatusType.PENDING
        ).first()
        if friend:
            FriendService.reject_request(friend)
            service = NotificationService(request)
            service.post(
                sender=friend.sender,
                receiver=friend.receiver,
                category=NotificationCategoryType.REJECT
            )
        return redirect("friends:read_friends_list")
        
@login_required
def read_friend_detail(request, username):
    friend_user = CustomUser.objects.filter(username=username).first()
    if not friend_user:
        messages.error(request, "존재하지 않는 사용자입니다.")
        return redirect("friends:read_friends_list")

    # 핸들러로 운동 목표 label 리스트 추출
    goal_handler = JSONIntChoicesListHandler(friend_user, 'exercise_goal', ExerciseGoalType)
    exercise_goals = goal_handler.get_display_names_safe()

    context = {
        "friend_user": friend_user,
        "exercise_goals": exercise_goals,
    }
    return render(request, "friend_detail.html", context)

