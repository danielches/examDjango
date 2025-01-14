# views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def homepage_view(request):
    searchform = SearchForm()
    genres = Genre.objects.all()
    booklist = Book.objects.all().order_by('-buy_cnt')[:3]
    return render(request, 'homepage.html', {'booklist': booklist, 'genres': genres,
                                             'searchform': searchform})

def all_books_view(request):
    all_books = Book.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(all_books, 12)  # Display 12 books per page
    page_obj = paginator.get_page(page_number)
    genres = Genre.objects.all()
    searchform = SearchForm()

    return render(request, 'books.html', {
        'title': 'All Books',
        'books': page_obj,
        'genres': genres,
        'searchform': searchform
    })


def popular_books_view(request):
    popular_books = Book.objects.all().order_by('-buy_cnt')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(popular_books, 12)  # Display 12 books per page
    page_obj = paginator.get_page(page_number)
    genres = Genre.objects.all()
    searchform = SearchForm()

    return render(request, 'books.html', {
        'title': 'Popular Books',
        'books': page_obj,
        'genres': genres,
        'searchform': searchform

    })

def bookpage_view(request, book_id):
    searchform = SearchForm()
    genres = Genre.objects.all()
    book = get_object_or_404(Book, id=book_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            book.buy_cnt += 1
            book.save()
            cart_item.save()
            return redirect('cart_detail')

    else:
        form = AddToCartForm()

    return render(request, 'bookpage.html',
                  {'form': form, 'book': book, 'genres': genres, 'searchform': searchform})


def genrepage_view(request, genre_code):
    searchform = SearchForm()
    genres = Genre.objects.all()
    books = Book.objects.filter(genre__code=genre_code)
    return render(request, 'genrepage.html', {'books': books, 'genres': genres, 'searchform': searchform})


def search_books(request):
    searchform = SearchForm()
    genres = Genre.objects.all()
    books = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(
                models.Q(title__icontains=query) |
                models.Q(author__icontains=query) |
                models.Q(description__icontains=query) |
                models.Q(genre__name__icontains=query)
            ).distinct()

    return render(request, 'search.html',
                  {'searchform': searchform, 'books': books, 'query': form.cleaned_data['query'],
                   'genres': genres})


@login_required
def cartpage_view(request):
    searchform = SearchForm()
    genres = Genre.objects.all()
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart, 'genres': genres,
                                                'searchform': searchform})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_detail')
