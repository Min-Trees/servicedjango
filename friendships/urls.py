from django.urls import path
#from .views import CreateFriendRequestView, FriendsAndFriendRequestsView, get_friends, request_friend
from .views import ListFriends, Friends_list
urlpatterns = [
    #path('list-friendship/', get_friends, name = 'list-friendship'),
    #path('request-friendship/',request_friend, name = 'request-friend'),
    #path('send-friend-request/', CreateFriendRequestView.as_view(), name='send_friend_request'),
    #path('friends-and-friend-requests/', FriendsAndFriendRequestsView.as_view(), name='friends_and_friend_requests'),
    path('list-friends/<str:user_id>/', ListFriends, name='list-friends'),
    path('friends/<str:user_id>/',Friends_list, name = 'friends-list'),
]
