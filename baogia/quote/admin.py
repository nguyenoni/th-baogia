from django.contrib import admin
from django.db import models
from .models import Category, Product, Service_Costs
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug", "create_at", "is_activate",]
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","create_at","update_at","is_activate",]
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Service_Costs)
class Service_Costs(admin.ModelAdmin):
    list_display = ["name","price_material","create_at","update_at","is_activate",]
    search_fields = ('name',)
    ordering = ('id',)