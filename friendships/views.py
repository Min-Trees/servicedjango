from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from users.models import Account
from rest_framework import generics, status
from .serializers import RequestFriendShipSerializer
from .models import Request, Friends
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class SendRequest(generics.CreateAPIView):
    serializer_class = RequestFriendShipSerializer

    def Create(self, request, *args, **kwargs):
        to_user_id = self.kwargs['to_user_id']
        to_user = get_object_or_404(Account, id = to_user)

        if request.user != to_user:
            friend_request_exits = Request.objects.filter(
                requester = request.user, receiver = to_user, accepted = False
            ).exists()

            if not friend_request_exits:
                friend_request = Request(requester = request.user, receiver= to_user)
                friend_request.save()
                return Response({'message': 'Lời mời kết bạn đã được gửi'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Lời mời kết bạn đã tồn tại'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Bạn không thể tự gửi lời mời kết bạn cho chính mình'}, status=status.HTTP_400_BAD_REQUEST)
        
def ListFriends(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    
    sent_requests = Request.objects.filter(requester=user, status='accepted')
    received_requests = Request.objects.filter(receiver=user, status='accepted')

    friends_from_sent_requests = [request.receiver for request in sent_requests]
    friends_from_received_requests = [request.requester for request in received_requests]
    
    all_friends = friends_from_sent_requests + friends_from_received_requests
    friends, created = Friends.objects.get_or_create(user=user)
    unique_friends = list(set(all_friends))
    friends.friends.set(unique_friends)

    friends_data = [{'id': friend.id, 'name': friend.name} for friend in unique_friends]
    
    return JsonResponse({'friends': friends_data})

def Friends_list(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    
    # Lấy danh sách bạn bè của người dùng
    try:
        friends = Friends.objects.get(user=user)
        friend_accounts = friends.friends.all()
    except Friends.DoesNotExist:
        friend_accounts = []

    # Xây dựng danh sách bạn bè dưới dạng JSON
    friends_data = [{'id': friend.id, 'name': friend.name} for friend in friend_accounts]
    
    return JsonResponse({'friends': friends_data})