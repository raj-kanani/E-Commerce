from django.contrib import admin
from .models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(CartItem)
class CartListAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cart', 'product', 'quantity', 'price', 'total_price']
