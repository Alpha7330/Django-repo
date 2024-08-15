from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
  path('authors/',AuthorView.as_view()),#authors
  path('authors/<int:id>/',author_detail_view.as_view()),#authors
  path('books/',BookListCreate.as_view()),#books
  path('books/<int:id>/',BookDetail.as_view()),#books
  path('user/',Userlist_create.as_view()),#users
  path('user/<int:pk>/',Userdis_up_del.as_view()),#users
  path('send_email/',SendEmailView.as_view()),
  path('library/',LibraryView.as_view()),#library
  path('library/<int:id>/',detail_libary_view.as_view()),#library
  path('librarians/',libraians_view.as_view()),#librarians
  path('librarians/<int:id>/',detail_libraians_view.as_view()),#libraians
  
  path('get/authors/<int:pk>',AuthorAPIView.as_view()),#authors
  path('get/all/authors', AuthorAPIView.as_view()),#authors
  path('get/all/books', BookAPIView.as_view()),#books
  path('get/books/<int:pk>', BookAPIView.as_view()),#books

]