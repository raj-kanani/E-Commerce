from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from address.models import Address
from cart.models import CartItem


class Checkout(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
