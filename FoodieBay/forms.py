# pylint: disable=bad-indentation,trailing-whitespace, too-few-public-methods,missing-final-newline
"""Forms.py class"""
from django import forms
from .models import fooditem

class FooditemForm(forms.ModelForm):
   """Forms for food items are defined here"""
   class Meta:
       """food items schema defined here"""
       model = fooditem
       fields = ['item_name', 'description', 'price', 'image', 'non_veg']
       
   def get_item_name(self):
       """Return item name from form"""
       return self.cleaned_data.get('item_name')