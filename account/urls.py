from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
app_name = 'accounts'
urlpatterns = [
    path('registration/', RegistrationView, name='registration'),
    path('', LoginView.as_view(template_name='account/login.html'), name='login_user'),
    path('logout_out', LogoutView.as_view(template_name='account/logged_out.html'), name='logout'),
]
