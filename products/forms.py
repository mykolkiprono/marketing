from django import forms
from . import models

class product_form(forms.ModelForm):
    class Meta:
        model = models.product
        fields = ['name','desc','available_stock','price','delivery','delivery_radius']
