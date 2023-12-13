from django.urls import path
from .views import  create_user,  SearchUser, Delete_user, UpdateUser, GetProfile,GetAuthenticatedUser
urlpatterns = [
    # return user
    path('v2/user/create',create_user,name='register'),
    path('search',SearchUser,name='SearchUser'),
    path('delete/<str:user_id>',Delete_user,name='delete-user'),
    path('v2/user/profile/',GetProfile,name='profile'),
    path('update/<str:user_id>', UpdateUser, name = 'update-user'),
    path('v2/user/authenticated/',GetAuthenticatedUser,name='authenticated')
    #get user from auth
]
