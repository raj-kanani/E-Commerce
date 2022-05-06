from django.contrib import admin
from .models import *


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_id', 'payment_method', 'payment_status', 'total_amount', 'created_at',
                    'updated_at']


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'product', 'product_amount']
