from django.urls import path
from products.views import Products_create,ProductsList_view,ProductView_detail, Products_edit, ProductDelete

app_name = 'products'

urlpatterns = [
    path('', ProductsList_view.as_view(),name= 'list'),
    path('<int:pk>/', ProductView_detail.as_view(),name="cart_product"),
    path('add_product/', Products_create.as_view(),name="add_product"),
    path('edit_product/<int:pk>', Products_edit.as_view() ,name="edit_product"),
    path('delete_product/<int:pk>', ProductDelete.as_view(),name="delete_product"),
]
