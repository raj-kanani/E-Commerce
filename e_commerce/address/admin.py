from django.contrib import admin
from .models import *


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'city', 'state', 'pincode']
