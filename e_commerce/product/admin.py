from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'description', 'product_price', 'product_image']
