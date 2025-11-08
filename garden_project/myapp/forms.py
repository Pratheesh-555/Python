from django import forms
from .models import Plant_Details

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant_Details
        fields = '__all__'
        widgets = {
            "plantname" : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the plant name"}),
            "planttype" : forms.Select(attrs={"class" : "form-control"}),
            "plantprice" : forms.NumberInput(attrs={"class" : "form-control","placeholder" : "Enter th plant price"}),
        }
