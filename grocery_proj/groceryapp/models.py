from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rpu = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name