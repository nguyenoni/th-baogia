from django.urls import path
from django.urls.conf import path, re_path
from .views import list_category, detail_category, load_volume_product

urlpatterns = [
    path('', list_category.as_view(), name='list_category'),
    path('<slug:slug>', detail_category, name='detail_category'),
    path('api/load-volume-product/', load_volume_product, name="load_volume_product")
    
]
