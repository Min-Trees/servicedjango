from django.db import models
from django.contrib.auth.models import Permission
import uuid
from django.utils import timezone

'''class FriendShip(models.Model):
    user1 = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='user1_friendships')
    user2 = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='user2_friendships')
    status = models.CharField(max_length=10, default='pending')'''

class Account(models.Model):
    #gender_choice
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    OTHER = 'OTHER'
    #type_role_choice
    TYPE_ROLE = [
        (STUDENT , 'STUDENT'),
        (TEACHER , 'TEACHER'),
        (OTHER , 'OTHER'),

    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200) # service friends
    role = models.CharField(max_length=100,default='NORMAL')
    birthday = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    type = models.CharField(max_length=10,choices=TYPE_ROLE,null=True)
    department = models.CharField(max_length=100, null=True, default=None)
    classroom = models.CharField(max_length=100, null=True, default=None)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now_add=True)
