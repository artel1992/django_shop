from django.shortcuts import render
from products.models import Products
from main.fucntions import MenuList
from products.forms.products import AddProducts
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy


class ProductsList_view(ListView):
    model = Products
    template_name = 'products/index.html'
    paginate_by = 3



class ProductView_detail(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'products/product_cart.html'



class Products_create(CreateView):
    model = Products
    form_class = AddProducts
    success_url = reverse_lazy('products:list')
    template_name = 'products/add_product.html'


class Products_edit(UpdateView):
    model = Products
    fields = ['name', 'price', 'description','image','categories']
    success_url = reverse_lazy('products:list')
    template_name = 'products/add_product.html'


class ProductDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('products:list')
    template_name = 'products/delete_product.html'


def ProductsListView(request):
    menu = MenuList()
    path = request.path
    products = Products.objects.all()
    return render(
        request, 'products/index.html', locals()
    )
