from django.db import models
from users.models import Account

class FriendShips(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user', null = True)
    friend = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='friend', default=0)

class RequestFriendShip(models.Model):
    requester = models.ForeignKey(Account,related_name='requester', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='receiver', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

class FriendRequest(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='received_friend_requests')
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])

    def to_dict(self):
        return {
            'senderID': self.sender.id,
            'receiverID': self.receiver.id,
            'status': self.status,
        }

