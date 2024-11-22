from django import forms
from .models import fooditem

class FooditemForm(forms.ModelForm):
    class Meta:
        model = fooditem
        fields = ['item_name', 'description', 'price', 'image', 'non_veg']
