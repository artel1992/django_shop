from django.contrib import admin
from django.template.loader import render_to_string
from .models import Products,Categories
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'categories',
        'price',
         'picture',
        'created',
        'modified',
        'is_new',
    ]
    list_filter = ['categories','created','modified']
    search_fields = ['name']
    fieldsets = (
        ('Base',{'fields':('name','categories')}),
    )
    def picture(self,obj):
        return render_to_string(
            'products/compontnts/picture.html',
            {
                'link':obj.image
            }
        )
    def is_new(self,obj):
        return obj.modified == obj.created
class ProductInline(admin.TabularInline):
    model = Products

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    search_fields = ['title']
    inlines = [ProductInline]
    def is_new(self,obj):
        return obj.modified == obj.created

admin.site.register(Products,ProductAdmin)
admin.site.register(Categories,CategoryAdmin)