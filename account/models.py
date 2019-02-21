from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils.timezone import now


class AccountUser(AbstractUser):
    birth_date = models.DateField(verbose_name='Дата рождения',null=True,blank=True)
    img = models.ImageField(upload_to='accounts',null=True,blank=True)
