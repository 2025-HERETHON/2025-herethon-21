from .models import Friend
from utils.choices import FriendStatusType

class FriendService:
    @staticmethod
    def send_request(sender, receiver):
        if sender == receiver:
            raise ValueError("본인에겐 친구 요청할 수 없습니다.")
        
        if Friend.objects.filter(sender=sender, receiver=receiver).exists():
            raise ValueError("이미 친구 요청을 보냈습니다.")
        
        Friend.objects.create(
            sender=sender,
            receiver=receiver,
            status=FriendStatusType.PENDING
        )
        
    @staticmethod
    def accept_request(friend):
        friend.status = FriendStatusType.ACCEPT
        friend.save()
        
    @staticmethod
    def reject_request(friend):
        friend.delete()