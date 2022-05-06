from decimal import Decimal
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def _get_total_price(self):
        sub_total = 0
        for i in self.cart_items.all():
            sub_total += i.price
        return sub_total

    total_price = property(_get_total_price)

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)

    @property
    def __int__(self):
        price = self.price
        quantity = self.quantity
        # total_price = self.total_price
        total_price = price * quantity
        print(total_price, '---------------------&**&&*&*&*&*&*&*&*&-------------')
        return total_price
