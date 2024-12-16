# models.py
from django.db import models


class Genre(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    photo = models.ImageField(upload_to='images/')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title
