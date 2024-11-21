from django.contrib import admin

# Register your models here.

from .models import fooditem, Contact, Order

admin.site.register(fooditem)
admin.site.register(Contact)
admin.site.register(Order)