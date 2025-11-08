from django.db import models

# Create your models here.

class Plant_Details(models.Model):
    plantName = models.CharField(max_length=100)
    plantPrice = models.IntegerField()
    plantBenefits = models.CharField(max_length=300)
    
    types = [
        ('Fruit', 'Fruit'),
        ('Veg', 'Veg'),    
        ]
    plantType = models.CharField(max_length=100,choices = types)


    def __str__(self):
        return f"{self.plantName} is the name.\n"

