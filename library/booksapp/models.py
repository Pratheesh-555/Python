from django.db import models

# Create your models here.

class Book(models.Model):
    TYPES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices = TYPES)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    total = models.DecimalField(decimal_places=2, max_digits=10)

    