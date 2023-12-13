from celery import Celery
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import User_Operation
from datetime import datetime
app = Celery('friendships')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

def send_realtime_event(user_id,action, message):
    channel_layer = get_channel_layer()
    group_name = f"user_{user_id}"

    async_to_sync(channel_layer.group_send)(
        group_name ,{
            'type':'friendship_event',
            'action':action,
            'message': message,
        }
    )

@app.task
def send_friend_request_event(to_user_id):
    send_realtime_event(to_user_id,'friend_request_send','Friend request sent')

def update_user_operation(user_id, online):
    user_operation , create = User_Operation.objects.get_or_create(id = user_id)
    user_operation.operation =  online
    user_operation.last_update = datetime.now()
    user_operation.save()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {
            'type': 'update_user_operation',
            'user_id': user_id,
            'operation': online,
        }
    ) 