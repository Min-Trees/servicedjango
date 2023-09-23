from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from friendships.serializers import FriendShipSerializers
from users.models import Account
from .models import FriendRequest, FriendShips, RequestFriendShip
from django.contrib.auth.models import User
from rest_framework.views import APIView
class CreateFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        receiver_id = request.data.get('receiver_id')
        receiver = Account.objects.get(id=receiver_id)

        FriendRequest.objects.create(
            sender=request.user,
            receiver=receiver,
            status='pending',
        )

        return Response({'status': 'Friend request sent'}, status=201)

'''class FriendsAndFriendRequestsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        friends = Account.objects.filter(friends=request.user)
        friend_requests = FriendRequest.objects.filter(sender=request.user)

        return Response({
            'friends': [friend.to_dict() for friend in friends],
            'friend_requests': [friend_request.to_dict() for friend_request in friend_requests],
        })'''

@api_view(['GET'])
def request_friend(request):
    user = request.user
    friends = RequestFriendShip.objects.filter()
def get_friends(request):
    user = request.user

    friends = user.friends.all()
    serializer = FriendShipSerializers(friends, many=True)
    return JsonResponse(serializer.data, safe=False)

class FriendsAndFriendRequestsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        userID = request.GET.get('userID')

        if not userID:
            return Response({'error': 'userID is required'}, status=400)

        friends = Account.objects.filter(friends=userID)
        friend_requests = FriendRequest.objects.filter(sender=userID)

        return Response({
            'friends': [friend.to_dict() for friend in friends],
            'friend_requests': [friend_request.to_dict() for friend_request in friend_requests],
        })
    