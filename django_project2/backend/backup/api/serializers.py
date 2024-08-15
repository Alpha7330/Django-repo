from rest_framework import serializers
from .models import *
class showroomserializer(serializers.ModelSerializer):
    class Meta:
        model=Showroom
        fields="__all__"

class carserializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields="__all__"