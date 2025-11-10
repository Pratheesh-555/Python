from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    return render(request, 'booksapp/index.html')

def update(request):
    if request.method == "POST:
        form = Book.getobjects.all()
        if 
    return render(request, 'booksapp/update.html')

