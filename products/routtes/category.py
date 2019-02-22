from django.urls import path
from products.views import RestCategoryListView
app_name = 'rotes_category'
urlpatterns=[
path('',RestCategoryListView.as_view(),name='list')
]