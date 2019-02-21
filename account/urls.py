from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView
app_name = 'accounts'
urlpatterns = [
    path('registration/', RegistrationView, name='registration'),
    path('', LoginView.as_view(template_name='account/login.html'), name='login_user'),
]
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]