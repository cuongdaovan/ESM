from rest_framework import serializers

from django.contrib.auth.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255)
    refresh_token = serializers.CharField(max_length=255)
