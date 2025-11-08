from .models import Grocery
from django import forms


class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'quantity', 'rpu']
        widgets = {
            'name' : forms.TextInput(attrs={"class" : "form-control"}),
            'quantity' : forms.NumberInput(attrs={"class" : "form-control"}),
            'rpu' : forms.NumberInput(attrs={"class": "form-control"}),
        }