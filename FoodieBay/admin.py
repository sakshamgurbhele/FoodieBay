from django.contrib import admin

# Register your models here.

from .models import fooditem, Contact

admin.site.register(fooditem)
admin.site.register(Contact)