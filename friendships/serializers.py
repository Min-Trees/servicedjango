from rest_framework import serializers
from .models import FriendShips , RequestFriendShip
class FriendShipSerializers(serializers.Serializer):
    class Meta:
        model = FriendShips
        field = '__all__'
        
class RequestFriendShipSerializer(serializers.Serializer):
    class Meta:
        model = RequestFriendShip
        field = '__all__'
