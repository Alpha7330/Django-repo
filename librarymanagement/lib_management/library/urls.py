from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("Books/", views.book_tab, name="books"),
    path("Authors/", views.Authors, name="authors"),
    path("Users/", views.user_tab, name="users"),
    path("Librarians/", views.Librarians, name="librarians"),
    path("Users/add/",views.save_user, name="save_user"),
    path("Books/add/", views.save_book, name="save_book"),
]    