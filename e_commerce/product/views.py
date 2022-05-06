from rest_framework import viewsets
from .serializers import *


class ProductCRUD(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
