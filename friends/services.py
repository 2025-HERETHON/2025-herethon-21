from .models import Friend
from utils.choices import FriendStatusType
from django.db.models import Q
from notifications.services import NotificationService
from utils.choices import NotificationCategoryType

class FriendService:
    @staticmethod
    def send_request(request, sender, receiver):
        if sender == receiver:
            raise ValueError("본인에게 친구 요청을 보낼 수 없습니다.")

        # "서로가" 이미 수락된 친구 관계인지 확인
        if Friend.objects.filter(
            (Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender)),
            status=FriendStatusType.ACCEPT
        ).exists():
            raise ValueError("이미 친구입니다.")

        # "내가" 이미 요청 보낸 경우
        if Friend.objects.filter(sender=sender, receiver=receiver).exists():
            raise ValueError("이미 친구 요청을 보냈습니다.")

        # 새로운 요청 생성
        Friend.objects.create(
            sender=sender,
            receiver=receiver,
            status=FriendStatusType.PENDING
        )
        
        NotificationService(request).post(
            sender=sender,
            receiver=receiver,
            category=NotificationCategoryType.REQUEST
        )
        
    @staticmethod
    def accept_request(request, friend):
        friend.status = FriendStatusType.ACCEPT
        friend.save()   
             
        NotificationService(request).post(
            sender=friend.sender,
            receiver=friend.receiver,
            category=NotificationCategoryType.ACCEPT
        )
        
    @staticmethod
    def reject_request(request, friend):
        friend.delete()
        
        NotificationService(request).post(
            sender=friend.sender,
            receiver=friend.receiver,
            category=NotificationCategoryType.ACCEPT
        )