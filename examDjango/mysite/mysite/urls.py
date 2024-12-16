from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from books.views import *

from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage_view, name='home'),
    path('book/<int:book_id>/', bookpage_view, name='book'),
    path('genre/<str:genre_code>/', genrepage_view, name='genre'),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
