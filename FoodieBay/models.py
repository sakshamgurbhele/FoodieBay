from django.db import models
import datetime
from django.utils.timezone import now
import uuid


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

# Contacts
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField()

# Order Ids
class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=now, editable=False)
    items = models.JSONField()  # Stores cart items in JSON format
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order_id)