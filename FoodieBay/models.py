from django.db import models
import datetime


# Create your models here.

# Fooditems
class fooditem(models.Model):
    item_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, default=0, decimal_places=2)
    image = models.ImageField(upload_to='uploads/product/',  default='')
    non_veg = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_name
