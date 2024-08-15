from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return render(request, 'index.html',context={'current_tab':'home'})
def Authors(request):
    return render(request, 'authors.html',context={'current_tab':'Authors'})
def Librarians(request):
    return render(request, 'librarians.html',context={'current_tab':'Librarians'})

def user_tab(request):
    if request.method == 'GET':
        users=User.objects.all()
        return render(request, 'users.html',context={'current_tab':'Users' ,'users':users})
    else:
        query=request.POST.get('query')
        users = User.objects.filter(user_name__icontains=query)
        return render(request, 'users.html',context={'current_tab':'Users' ,'users':users})

def save_user(request):
    item=User(reference_id=request.POST.get('reference_id'),
              user_name=request.POST.get('user_name'),
              user_contact=request.POST.get('user_contact'),
              user_address=request.POST.get('user_address'),
              active=True)
    item.save()

    return redirect('users')

def book_tab(request):
    if request.method == 'GET':
        books=Book.objects.all()
        return render(request,'books.html',context={'current_tab':'Books' ,'books':books})
    else:
        query=request.POST.get('query')
        books = Book.objects.filter(book_name__icontains=query)
        return render(request,'books.html',context={'current_tab':'Books' ,'books':books})

def save_book(request):
    bk=Book(book_name=request.POST.get('book_name'),
              author_name=request.POST.get('author_name')
            
              ) 
    bk.save()

    return redirect('books')