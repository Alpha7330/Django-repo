from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Please enter an email address")
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if not extra_fields.get('is_staff'):
            raise ValueError('is_staff must be set to True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('is_superuser must be set to True')
        if not extra_fields.get('is_active'):
            raise ValueError('is_active must be set to True')
        
        return self.create_user(email,password,**extra_fields)