from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import random
# Create your models here.


    

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        super().save(*args, **kwargs)

    def is_valid(self):
        return timezone.now() < self.created_at + datetime.timedelta(minutes=10)
    
    def __str__(self):
        return f"{self.user.username} - {self.token}"

