from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import *
from main.fucntions import MenuList

def Registrations(request):
    menu = MenuList()
    if request.method =='POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
        #else:
            #for error in form.errors:
                # if error in form.fields :
                #     if form.errors[error].data[0].code == 'unique':
                #         form.errors[error][0] = 'Пользователь с уникальным полем( ' + str(form.fields[error].label)+' ) уже сужествует'
                #     else:
                #         form.errors[error][0] = 'Не корекктное поле: ' + str(form.fields[error].label)
    else:
        form = RegistrationForm()
    return render(request,'account/registration.html',locals())


def Login_View(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password = password
            )
            if user and user.is_active:
                login(request=request,user=user)
                return reverse('main:home')


    return render(request,'account/login.html',locals())

def RegistrationView(request):
    form = RegistrationUserForm()
    if request.method == 'POST':
        user = form.save(commit=False)
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            user.is_active = True
            user = form.save()
        if user and user.is_active:
            login(request=request, user=user)
            return reverse('main:home')


    return render(request,'account/registration.html',locals())