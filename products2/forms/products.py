from products.models import *
from django import forms

class AddProducts(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name','description','price','image','categories')
        widgets = {
            'name':forms.widgets.TextInput(),
            'description': forms.widgets.Textarea(),
            'price':forms.widgets.NumberInput(),
            'image': forms.widgets.FileInput(),
            'categories':forms.widgets.Select()
        }
