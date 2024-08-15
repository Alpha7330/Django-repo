from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from enum import IntEnum
from .managers import UserManager
# Create your models here.

class Gender(IntEnum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]






# class UserManager(BaseUserManager):
#     def create_user(self,email,password,**extra_fields):
#         if not email:
#             raise ValueError("Please enter an email address")
        
#         email=self.normalize_email(email)
#         user=self.model(email=email,**extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    

#     def create_superuser(self,email,password,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         if not extra_fields.get('is_staff'):
#             raise ValueError('is_staff must be set to True')
#         if not extra_fields.get('is_superuser'):
#             raise ValueError('is_superuser must be set to True')
#         if not extra_fields.get('is_active'):
#             raise ValueError('is_active must be set to True')
        
#         return self.create_user(email,password,**extra_fields)
    

class CustomUser(AbstractBaseUser):   
    
    email=models.EmailField(max_length=200,unique=True)
    first_name=models.CharField(max_length=45,null=True,blank=True)
    last_name=models.CharField(max_length=45,null=True,blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    gender=models.SmallIntegerField(choices=Gender.choices(),default=Gender.MALE.value)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['gender']

    objects=UserManager()

    def __str__(self):
        return self.email
    
    def has_module_perms(self,app_label):
        return True
    
    def has_perm(self,perm,obj=None):
        return True