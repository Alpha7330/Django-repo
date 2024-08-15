from django.db import models

# Create your models here.
class User(models.Model):
    reference_id = models.CharField(max_length=200 ,default=None)
    user_name = models.CharField(max_length=200 ,default=None)
    user_contact = models.CharField(max_length=200 ,default=None)
    user_address = models.TextField(default=None)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.user_name
    
class Author(models.Model):
    author_name = models.CharField(max_length=200)    

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name=models.CharField(max_length=200)

    def __str__(self):
        return self.book_name
    


class Borrow(models.Model):
    member=models.ForeignKey(User, on_delete=models.CASCADE)
    book_br=models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book_br} by{self.member}"