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
    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('ADMIN', 'Admin'),
    ]
    # user-information TDMU
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200) 
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    background_url = models.URLField(blank=True, null=True)
    following = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)
    
    birthday = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    #social
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES)
    #school
    school_name = models.TextField(blank=True, null=True)
    school_faculty = models.TextField(blank=True, null=True)
    school_majors  = models.TextField(blank=True, null=True)

    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now_add=True)
