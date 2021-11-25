from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

from accounts.models import HairImage

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        # model = get_user_model()
        model = get_user_model()
        fields= ('username','password')

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'
