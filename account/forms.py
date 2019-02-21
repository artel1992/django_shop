from django.contrib.auth.forms import UserCreationForm

from .models import *
from django import forms



class RegistrationForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'birth_date', 'img')
        widgets ={
            'username':forms.widgets.TextInput(attrs={'class':"form-contol "}),
            'password1':forms.widgets.PasswordInput(attrs={'class':"form-contol "}),
            'password2':forms.widgets.PasswordInput(attrs={'class':"form-contol "}),
            'birth_date':forms.widgets.DateInput(attrs={'class':"form-contol "}),#Не могу понять почему получается текстовый инпут а не дата(((((
            'img':forms.widgets.FileInput(attrs={'class':"form-contol "})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''

        def clean_age(self):
            data = self.cleaned_data['birth_date']
            if data < 18:
                raise forms.ValidationError("Вы слишком молоды!")
            return data

class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=128)
    password = forms.CharField(required=True,max_length=128,widget=forms.widgets.PasswordInput())

class RegistrationUserForm(forms.ModelForm):
    password_cinfirm = forms.CharField(required=True,max_length=75,widget=forms.widgets.PasswordInput)
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password is not confirm')

        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationUserForm,self).save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        if commit:
            user.save()
        return user
    class Meta:
        model = AccountUser
        fields = ('username', 'password')
        widgets ={
            'username':forms.widgets.TextInput(attrs={'class':"form-contol "}),
            'password':forms.widgets.PasswordInput(attrs={'class':"form-contol "}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''

        def clean_age(self):
            data = self.cleaned_data['birth_date']
            if data < 18:
                raise forms.ValidationError("Вы слишком молоды!")
            return data