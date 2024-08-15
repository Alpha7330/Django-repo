from django.urls import path
from .views import *
urlpatterns = [
    path('otp/',GenerateOtp.as_view()),
    path('verify-otp/', VerifyOtp.as_view(), name='verify-otp')
]
