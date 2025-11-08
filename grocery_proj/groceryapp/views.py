from django.shortcuts import render, redirect
# Create your views here.
from .models import Grocery
from .forms import GroceryForm 

def home(request):
    return render(request, 'groceryapp/index.html')

def show(request):
    list = Grocery.objects.all()
    return render(request, 'groceryapp/show.html', {'items' : list})

def insert(request):
    if request.method == "POST":
        form = GroceryForm(request.POST)
        grocery = form.save(commit=False)
        if form.is_valid():
            grocery.amount = grocery.quantity * grocery.rpu
            grocery.save()
            return redirect('show')
    else:
        form = GroceryForm()
    return render(request, 'groceryapp/insert.html', {'form' : form})

def update(request, id):
    grocery = Grocery.objects.get(id=id)
    if request.method == "POST":
        form = GroceryForm(request.POST, instance = grocery)
        if form.is_valid():
            grocery = form.save(commit=False)
            grocery.amount = grocery.quantity * grocery.rpu
            grocery.save()
            return redirect('show')
    else:
        form = GroceryForm(instance = grocery)
    return render(request, 'groceryapp/update.html', {'form' : form})

