from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from .models import Announced, Category, FeeShipping, Material, PackagingLevel1, PackingWorker, Product, Stamp, Volume, PackagingLevel2
from django.views.generic.detail import DetailView
from . import libs

# Create your views here.

class list_category(View):

    def get(self, request):
        tmp = "quote/category.html"
        obj_category = Category.objects.all()
        if(obj_category):
            return render(request, tmp, {"data": obj_category})


def detail_category(request, slug):
    tmp = "quote/create-quote.html"
    if(slug and Category.objects.filter(slug = slug)[0]):
        obj_category = Category.objects.filter(slug=slug)[0]
        obj_product = Product.objects.filter(category = obj_category)

    return render(request, tmp, {"data": obj_product})

# API get volume with UID product
def load_volume_product(request):
    contex={
        "status": 200,
        "message": "",
    }
    if(request.method == "POST" and request.POST.get('unique_product')):
        unique_product = request.POST.get('unique_product')
        try:
            obj_product = Product.objects.filter(unique_product = unique_product)[0]
            obj_volume = Volume.objects.filter(product = obj_product)
            contex.update({
                "data": libs.serializable(obj_volume),
                "message": "Load dung tích thành công!"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__(),
            })
        
        
    return JsonResponse({"data": contex})
# API load Material with volume, product id
def load_material(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_material = Material.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_material),
                "title": "Chọn nguyên liệu"
            })
            return JsonResponse({"data": contex})
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load packaging level 1
def load_packaging_level1(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_packaging_level1 = PackagingLevel1.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packaging_level1),
                "title": "Chọn bao bì cấp 1"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})
        
# API load packaging level 2
def load_packaging_level2(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_packaging_level2 = PackagingLevel2.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packaging_level2),
                "title": "Chọn bao bì cấp 2"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load stamp
def load_stamp(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_stamp = Stamp.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_stamp),
                "title": "Chọn gói tem nhãn"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load Nhân công đóng gói
def load_packing_worker(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_packing_worker = PackingWorker.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packing_worker),
                "title": "Chọn gói nhân công đóng gói"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load load_announced
def load_announced(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_announced = Announced.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_announced),
                "title": "Chọn gói công bố"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load FeeShip
def load_feeship(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_feeship = FeeShipping.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_feeship),
                "title": "Chọn gói vận chuyển"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})
