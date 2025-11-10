from django import forms
from .models import Book

class BookForm(models.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'price', 'quantity', 'total']