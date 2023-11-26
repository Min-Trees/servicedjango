from django.db import models
from users.models import Account

class Friends(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_friend')
    friends = models.ManyToManyField(Account, blank=True, related_name='friends_of')

class Request(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    
    REQUEST_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
    ]

    sender = models.ForeignKey(Account, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
