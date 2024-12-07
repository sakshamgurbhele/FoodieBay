# pylint: disable=bad-indentation,trailing-whitespace,missing-final-newline,unused-import,invalid-str-returned,invalid-name
"""Create your models here."""
import datetime
import uuid
from django.utils.timezone import now
from django.db import models





class fooditem(models.Model):
    """Fooditems define"""
    item_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, default=0, decimal_places=2)
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
    non_veg = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_name


class Contact(models.Model):
    """Contacts"""
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField()


class Order(models.Model):
    """Order Ids"""
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=now, editable=False)
    items = models.JSONField()  # Stores cart items in JSON format
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order_id)