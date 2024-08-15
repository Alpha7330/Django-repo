from django.contrib import admin

# Register your models here.
from .models import OtpToken

admin.site.register(OtpToken)