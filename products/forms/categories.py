from products.models import *
from django import forms






class AddCategory(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('title','description')
        widgets = {
            'title':forms.widgets.TextInput(),
            'description': forms.widgets.Textarea(),
        }