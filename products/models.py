from django.db import models
from django.db.models import Avg

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.TextField()
    location = models.CharField(max_length=25, default='')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    turnover = models.DecimalField(max_digits=15, decimal_places=2, default='0')
    net_profit = models.DecimalField(max_digits=15, decimal_places=2, default='0')
    image = models.ImageField(upload_to='images')
    brand = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name