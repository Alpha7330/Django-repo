from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EmailVerificationToken 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EmailVerificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerificationToken
        fields = ['user', 'token', 'created_at']
