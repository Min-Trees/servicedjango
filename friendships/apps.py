from django.apps import AppConfig


class FriendshipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'friendships'


class FriendsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'friendships'

    def ready(self):
        import friendships.signals
