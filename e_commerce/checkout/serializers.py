from .models import *
from rest_framework import serializers
from address.serializers import AddressSerializer


class CheckoutViewSerializer(serializers.ModelSerializer):
    address = AddressSerializer

    class Meta:
        model = Checkout
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    state = serializers.CharField(max_length=120)
    city = serializers.CharField(max_length=120)
    address = serializers.CharField(max_length=125)
    pincode = serializers.IntegerField()

    class Meta:
        model = Checkout
        fields = ['id', 'customer', 'cart', 'state', 'city', 'address', 'pincode']
