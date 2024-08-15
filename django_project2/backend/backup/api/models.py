from django.db import models

# Create your models here.

class Showroom(models.Model):
    showroom_name=models.CharField(max_length=50)
    showroom_email=models.EmailField(max_length=34)
    showroom_location=models.CharField(max_length=56)
    capacity=models.IntegerField()

    def __str__(self):
        return self.showroom_name
    

class Car(models.Model):
    showroom = models.ManyToManyField(Showroom, related_name='cars')
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'