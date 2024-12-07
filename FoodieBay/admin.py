# pylint: disable=bad-indentation,trailing-whitespace,missing-final-newline
"""Register your models here"""
from django.contrib import admin



from .models import fooditem, Contact, Order

admin.site.register(fooditem)
admin.site.register(Contact)
admin.site.register(Order)