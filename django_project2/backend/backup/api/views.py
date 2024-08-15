from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class showroomview(generics.ListCreateAPIView):
    queryset = Showroom.objects.all()
    serializer_class = showroomserializer


class showroomdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showroom.objects.all()
    serializer_class = showroomserializer
    lookup_field ='id'