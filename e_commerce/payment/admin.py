from django.contrib import admin
from .models import *


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_id', 'transaction_id', 'status', 'payment_type', 'payment_price']
