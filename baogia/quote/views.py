from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from .models import Category, Product, Volume
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