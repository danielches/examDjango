from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from books.views import *
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('book/<int:book_id>/', bookpage_view, name='book'),
    path('genre/<str:genre_code>/', genrepage_view, name='genre'),
    path('users/', include('users.urls', namespace='users')),
    path('search/', search_books, name='search_books'),
    path('popular/', popular_books_view, name='popular'),
    path('cart/', cartpage_view, name='cart_detail'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('books/', all_books_view, name='books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
