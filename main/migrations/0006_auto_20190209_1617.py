# Generated by Django 2.1.5 on 2019-02-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190209_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='order',
            field=models.IntegerField(default='0', verbose_name='Пордковый номер'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='link_name',
            field=models.CharField(max_length=255, verbose_name='Имя ссылки'),
        ),
    ]
