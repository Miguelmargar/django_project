from django.db import models
from django.db.models import Avg

# Create your models here.

class Product(models.Model):
    collection = models.CharField(max_length=25, default='')
    name = models.CharField(max_length=25, default='')
    description = models.TextField()
    case = models.CharField(max_length=25, default='')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    glass = models.CharField(max_length=25, default='')
    functions = models.CharField(max_length=25, default='')
    image = models.ImageField(upload_to='images')
    strap = models.CharField(max_length=25, default='')
    
    def __str__(self):
        return self.name