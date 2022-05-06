from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response


class CheckoutCreate(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckoutList(generics.ListAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def get(self, request, *args, **kwargs):
        checkout = Checkout.objects.all()
        serializer = CheckoutViewSerializer(checkout, many=True)
        return Response(serializer.data)
