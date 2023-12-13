# myproject/routing.py
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from friendships.consumers import FriendshipConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                path('ws/friendship/', FriendshipConsumer.as_asgi()),
            ]
        )
    ),
})
