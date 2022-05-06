from django.contrib import admin
from .models import *


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'cart', 'address']
