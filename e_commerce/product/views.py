from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *


class ProductCRUD(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
