from rest_framework import serializers
from .models import *
from address.serializers import AddressSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    user = AddressSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'
