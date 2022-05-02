from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets


# Create your views here.

class CartCreateList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def delete(self, request, pk):
        s = Cart.objects.get(pk=pk)
        s.delete()
        return Response(status=status.HTTP_200_OK, data={'msg': 'your cart item deleted'})


class CartCRUD(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartListSerializer
