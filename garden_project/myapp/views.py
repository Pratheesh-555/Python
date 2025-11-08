from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Plant_Details
from .forms import PlantForm

# Create your views here.
def plant_list(request):
    plants = Plant_Details.objects.all()
    return render(request, 'myapp/plant_list.html', {'plants': plants})

def insert(request):
    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    
    return render(request, 'myapp/insert.html', {'form' : form})

def update(request,id):
    plant = Plant_Details.objects.get(id=id)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
    return render(request, 'myapp/update.html', {'form' : form, 'plant' : plant})


def delete(request,id):
    plant = Plant_Details.objects.get(id=id)
    if request.method == "POST":
        plant.delete()
        return redirect('plant_list')
    return render(request, 'myapp/delete.html')