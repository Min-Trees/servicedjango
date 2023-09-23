from django.contrib import admin
from .models import FriendShips, RequestFriendShip, FriendRequest
# Register your models here.
admin.site.register(FriendShips)
admin.site.register(RequestFriendShip)
admin.site.register(FriendRequest)
