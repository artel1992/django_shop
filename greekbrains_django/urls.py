from django.contrib import admin
from django.urls import path, include
from products.views.categories import *
from django.conf import settings
from django.conf.urls.static import static
rutes = [
    path('category/',include('products.routtes.category'))
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('api/',include(rutes)),
    path('products/', include('products.urls.products')),
    path('categories/', include('products.urls.categories')),
    path('account/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)