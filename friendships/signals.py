from django.db.models.signals import post_save
from django.dispatch import receiver
from friendships.models import Friends
from users.models import Account

@receiver(post_save, sender=Friends)
def update_friends_list(sender, instance, **kwargs):
    if instance.user and instance.friends.exists():
        user = instance.user
        friends = instance.friends.all()
        user.friends.clear()  # Xóa tất cả bạn bè hiện tại của người dùng
        user.friends.add(*friends)