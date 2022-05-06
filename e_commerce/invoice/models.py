from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120)
    payment_method = models.CharField(max_length=150)
    payment_status = models.CharField(max_length=100)
    total_amount = models.FloatField(default=200.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.FloatField(default=0.0)

