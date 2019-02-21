from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', StartPage, name='home'),
    path('about/', AbouttPage,name='about'),
    path('contacts/', ContactsPage,name='contacts'),
]
