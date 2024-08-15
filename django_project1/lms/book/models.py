from django.db import models
from django.contrib.auth.models import AbstractUser   
# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200,default='indian')
    

    def __str__(self) :
        return f"{self.author_name}({self.nationality})"


class Books(models.Model):
    book_title = models.CharField(max_length=200)
    book_published_date=models.DateField()
    authors=models.ManyToManyField(Author,related_name="books")

    def __str__(self):
       return self.book_title

class User(models.Model):
    user_name = models.CharField(max_length=200) 
    books_borrowed= models.ManyToManyField(Books,related_name='users')
      

    def __str__(self):
        return self.user_name

class Library(models.Model):
    library_name = models.CharField(max_length=26)
    books_in_library =models.ManyToManyField(Books, blank=True, related_name='lib_books')
    def __str__(self):
        return self.library_name
    
class librarians(models.Model):
    librarians_name = models.CharField(max_length=37)
    library_con= models.ManyToManyField(Library,related_name='libraries')
    
    def __str__(self):
        return self.librarians_name

