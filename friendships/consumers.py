import json 
from channels.generic.websocket import AsyncWebsocketConsumer

class FriendshipConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data['action']

        if action == 'friend_request_send':
            await self.send(text_data=json.dumps({'message':'Lời mời kết bạn đã được gửi'}))
        elif action == 'friend_request_accepted':
            await self.send(text_data=json.dumps({'message': 'Lời mời kết bạn đã được chấp nhận'}))
        