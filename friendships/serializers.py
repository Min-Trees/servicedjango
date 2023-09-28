from rest_framework import serializers
from .models import Friends, Request
class FriendShipSerializers(serializers.Serializer):
    class Meta:
        model = Friends
        field = '__all__'
        
class RequestFriendShipSerializer(serializers.Serializer):
    class Meta:
        model = Request
        field = '__all__'

        