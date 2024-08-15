from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *
import random
from rest_framework.permissions import AllowAny


User = get_user_model()

class GenerateOtp(APIView):
    permission_classes = [AllowAny]
    def post(self,request, *args, **kwargs):
        email = request.data.get('email')

        try:
            user=User.objects.get(email=email)

        except User.DoesNotExist:
            return Response({"errors":"user with this email does not exist"},status=status.HTTP_400_BAD_REQUEST)    
        
        token,created=OtpToken.objects.get_or_create(user=user)

        if not created:
            token.token =''.join([random.choice('1234567890')for _ in range(6)])
            token.save()

        #send email
        send_mail('YOUR OTP CODE',
                  f'YOUR OTP CODE{token.token}.',
                  'alpha733060@gmail.com',
                  [user.email],
                  fail_silently=False
                  )
        
        serializer=OTPTokenSerializer(token)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class VerifyOtp(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        
        if not email or not otp:
            return Response({"errors": "Email and OTP are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            token = OtpToken.objects.get(user=user, token=otp)
            
            if not token.is_valid():
                return Response({"errors": "OTP has expired"}, status=status.HTTP_400_BAD_REQUEST)

            token.delete()  # Optionally invalidate OTP after use
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"errors": "User with this email does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except OtpToken.DoesNotExist:
            return Response({"errors": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
