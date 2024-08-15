from rest_framework import serializers
from .models import OtpToken

class OTPTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpToken
        fields = ['token']
