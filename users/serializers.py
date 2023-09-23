from rest_framework import serializers
from .models import Account , AccountProfile

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountProfile
        fields = '__all__'