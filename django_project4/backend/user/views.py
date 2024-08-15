from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import EmailVerificationToken
from .serializers import UserSerializer, EmailVerificationTokenSerializer
from django.conf import settings
import environ
env = environ.Env()
environ.Env.read_env('.env')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

@api_view(['POST'])
def send_verification_email(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
        token, created = EmailVerificationToken.objects.get_or_create(user=user)
        send_mail(
            'Your Verification Token',
            f'Your verification token is {token.token}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return Response({'detail': 'Token sent to email'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def verify_token(request):
    token = request.data.get('token')
    try:
        token_obj = EmailVerificationToken.objects.get(token=token)
        if token_obj.is_valid():
            token_obj.user.is_active = True
            token_obj.user.save()
            return Response({'detail': 'Token verified'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token expired or invalid'}, status=status.HTTP_400_BAD_REQUEST)
    except EmailVerificationToken.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)
