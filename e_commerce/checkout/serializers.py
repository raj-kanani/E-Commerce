from .models import *
from rest_framework import serializers

from address.serializers import AddressSerializer

from address.models import Address


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

    # def create(self, validated_data):
    #     cart = validated_data.pop('cart', None)
    #     print(cart)
    #     customer = validated_data.pop("customer", None)
    #     address = Address.objects.create(customer=customer,
    #                                      state=validated_data['state'],
    #                                      city=validated_data['city'],
    #                                      address=validated_data['address'],
    #                                      pincode=validated_data['pincode'],
    #                                      )
    #     print(cart)
    #     c = Checkout.objects.create(cart=cart, customer=customer, address=address, )
    #
    #     return address
