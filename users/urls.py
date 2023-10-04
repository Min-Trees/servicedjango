from django.urls import path
from .views import  getUser, getProfile, SearchUser, Delete_user, UpdateUser
urlpatterns = [
    # return user
    path('register',getUser,name='register'),
    path('search',SearchUser,name='SearchUser'),
    path('delete/<str:user_id>',Delete_user,name='delete-user'),
    path('update/<str:user_id>', UpdateUser, name = 'update-user'),
    #get user from auth
    path('getuser-profile', getProfile, name='getuser-profile'),
]
