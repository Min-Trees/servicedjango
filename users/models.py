from django.db import models
from django.contrib.auth.models import Permission
import uuid
from django.utils import timezone

'''class FriendShip(models.Model):
    user1 = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='user1_friendships')
    user2 = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='user2_friendships')
    status = models.CharField(max_length=10, default='pending')'''

class Account(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    
    id = models.CharField(primary_key=True,default=uuid.uuid4, max_length=36)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200) # service friends
    role = models.CharField(max_length=100,default='NORMAL')
    birthday = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now_add=True)

class AccountProfile(models.Model):
    # khi xoa user thi xoa luon cau profile cua user
    userID = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    userAvt = models.URLField(blank=True, null =True)
    userBackGround = models.URLField(blank=True, null=True)
