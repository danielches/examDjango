from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Book)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'photo', 'genre')
    list_display_links = ('id', 'title')


@admin.register(Genre)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')
    list_display_links = ('id', 'code', 'name')