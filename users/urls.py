from django.urls import path
from .views import UserViewDetail, getUser,Profile, deleteUserView, getProfile
urlpatterns = [
    # return user
    path('detail/<str:userID>/',UserViewDetail.as_view(),name='user-detail'),
    #http.... / api/detail/1
    path('delete-user/<str:userID>/',deleteUserView.as_view(),name='delete-user'),
    #get user from auth
    path('getuser-from-auth/',getUser,name='getuser-from-auth'),
    path('profile-user/<int:userID>/',Profile.as_view(), name='profile-user'),
    path('getuser-profile/', getProfile, name='getuser-profile'),

]
