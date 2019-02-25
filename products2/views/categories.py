from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Categories
from products.forms import AddCategory
from django.core.paginator import Paginator

class RestCategoryListView(ListView):
    model = Categories
    def ster(self,queryset):
        return list(map(
            lambda itm:{
                'id':itm.id,
                'title':itm.title
            },queryset
        ))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RestCategoryListView,self).get_context_data(**kwargs)
        object_list = context.get('object_list')
        data = {}
        data['results'] =self.ster(object_list)
        return data
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

class CategoriesList_view(ListView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'categories/index.html'

class CategoriesView_detail(DetailView):
    model = Categories
    template_name = 'categories/category.html'
    def get_context_data(self, **kwargs):
        key = self.context_object_name if self.context_object_name else 'object'
        obj = kwargs.get(key)
        products = obj.products_set.all()
        page = self.request.GET.get('page')
        paginator = Paginator(products,1)
        page_obj = paginator.get_page(page)
        return {key:obj,'products':page_obj}


class Categories_create(CreateView):
    model = Categories
    form_class = AddCategory
    success_url = reverse_lazy('categories:list')
    template_name = 'categories/add_category.html'

class Categories_edit(UpdateView):
    model = Categories
    fields = ['title','description']
    success_url = reverse_lazy('categories:list')
    template_name = 'categories/add_category.html'


class CategoriesDelete(DeleteView):
    model = Categories
    success_url = reverse_lazy('categories:list')
    template_name = 'categories/delete_category.html'