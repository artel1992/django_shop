from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    created =models.DateTimeField(
        auto_now_add=True #Создается в момент создания и больше не меняется
    )
    modified = models.DateTimeField(
        auto_now=True #Меняется каждый раз при изменении товара
    )
    image = models.ImageField(
        upload_to='products',
        blank=True,
        null=True
    )
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name





