from django.urls import path
from django.urls.conf import path, re_path
from .views import list_category, detail_category, load_packing_worker, load_volume_product, load_material, load_packaging_level1,load_packaging_level2, load_stamp

urlpatterns = [
    path('', list_category.as_view(), name='list_category'),
    path('<slug:slug>', detail_category, name='detail_category'),
    # API
    path('api/load-volume-product/', load_volume_product, name="load_volume_product"),
    path('api/load-material/', load_material, name="load_material"),
    path('api/load-packaging-level1/', load_packaging_level1, name="load_packaging_level1"),
    path('api/load-packaging-level2/', load_packaging_level2, name="load_packaging_level2"),
    path('api/load-stamp/', load_stamp, name="load_stamp"),
    path('api/load-packing-worker/', load_packing_worker, name="load_stamp"),



    
]
