from django.shortcuts import render
from products.models import Products
from main.fucntions import MenuList
from products.forms.products import AddProducts
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class ProductsList_view(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Products
    template_name = 'products/index.html'
    paginate_by = 3
    login_url = reverse_lazy('accounts:login_user')
    def test_func(self):
        return  self.request.user.has_perm('products.view_products')




class ProductView_detail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'products/product_cart.html'
    login_url = reverse_lazy('accounts:login_user')
    def test_func(self):
        return  self.request.user.has_perm('products.view_products')



class Products_create(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Products
    form_class = AddProducts
    success_url = reverse_lazy('products:list')
    template_name = 'products/add_product.html'
    login_url = reverse_lazy('accounts:login_user')
    def test_func(self):
        return  self.request.user.has_perm('products.add_products')


class Products_edit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Products
    fields = ['name', 'price', 'description','image','categories']
    success_url = reverse_lazy('products:list')
    template_name = 'products/add_product.html'
    login_url = reverse_lazy('accounts:login_user')
    def test_func(self):
        return self.request.user.has_perm('products.change_products')


class ProductDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Products
    success_url = reverse_lazy('products:list')
    template_name = 'products/delete_product.html'
    login_url = reverse_lazy('accounts:login_user')
    def test_func(self):
        return  self.request.user.is_superuser

@login_required(login_url=reverse_lazy('accounts:login_user'))
def ProductsListView(request):
    menu = MenuList()
    path = request.path
    products = Products.objects.all()
    return render(
        request, 'products/index.html', locals()
    )
@login_required(login_url=reverse_lazy('accounts:login_user'))
def test(request):
    pass