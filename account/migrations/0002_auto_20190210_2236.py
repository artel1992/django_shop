# Generated by Django 2.1.5 on 2019-02-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='accounts'),
        ),
    ]
