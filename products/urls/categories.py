from django.urls import path
from products.views.categories import CategoriesList_view, CategoriesView_detail, Categories_create, Categories_edit, CategoriesDelete


app_name = 'categories'

urlpatterns = [
    path('', CategoriesList_view.as_view(), name="list"),
    path('<int:pk>', CategoriesView_detail.as_view(), name="category"),
    path('add_category/', Categories_create.as_view(), name="add_category"),
    path('edit_category/<int:pk>', Categories_edit.as_view(), name="edit_category"),
    path('delete_category/<int:pk>', CategoriesDelete.as_view(), name="delete_category"),
]
