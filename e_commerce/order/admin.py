from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_choice', 'total']


@admin.register(OrderList)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'order', 'price', 'total_price']
