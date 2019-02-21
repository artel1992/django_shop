from django.db import models


# Create your models here.
class MainMenu(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название раздела меню")
    link_name = models.CharField(max_length=255,verbose_name='Имя ссылки')
    order = models.IntegerField(verbose_name='Пордковый номер',default='0')


    def __str__(self):
        return self.title
