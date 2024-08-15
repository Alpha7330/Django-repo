from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from datetime import timedelta
from django.utils import timezone
# Create your models here.


class OtpToken(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=6,unique=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.token:
            self.token=get_random_string(length=6,allowed_chars='1234567890')
            super().save(*args, **kwargs)

    def __str__(self):
        return self.token
    
    def is_valid(self):
        # Assuming OTP is valid for 10 minutes
        return timezone.now() < self.created_at + timedelta(minutes=10)