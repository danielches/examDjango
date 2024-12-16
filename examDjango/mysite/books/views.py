# views.py
from django.shortcuts import render
from .models import *


def homepage_view(request):
    booklist = Book.objects.all().order_by('-id')[:3]
    genrelist = Genre.objects.all()
    return render(request, 'homepage.html',{'booklist': booklist, 'genrelist': genrelist})


def bookpage_view(request, book_id):
    bookobj = Book.objects.get(id=book_id)
    return render(request, 'bookpage.html',{'book': bookobj})


def genrepage_view(request, genre_code):
    books = Book.objects.filter(genre__code=genre_code)
    return render(request, 'genrepage.html',{'books': books})
