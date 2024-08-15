from django.urls import path
from .views import send_verification_email, verify_token

urlpatterns = [
    path('api/token/', send_verification_email, name='send_verification_email'),
    path('api/verifytoken/', verify_token, name='verify_token'),
]

