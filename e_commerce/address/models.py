from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=125, default='Ahmedabad')
    state = models.CharField(max_length=125, default='Gujrat')
    pincode = models.IntegerField()

    def __str__(self):
        return self.address
