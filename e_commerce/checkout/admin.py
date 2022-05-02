from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'cart', 'address']
