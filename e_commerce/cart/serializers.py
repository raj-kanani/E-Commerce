from rest_framework import serializers
from .models import *
from product.models import Product


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

