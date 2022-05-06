from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *


# Create your views here.
class AddressCreate(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        add = Address.objects.all()
        serializer = AddressSerializer(add, many=True)
        return Response(serializer.data)


class AddresssUpdate(generics.RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def put(self, request, *args, **kwargs):
        add = Address.objects.get(pk=self.kwargs['pk'])

        serializer = AddressSerializer(add, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        add = Address.objects.get(pk=pk)
        add.delete()
        return Response(status=status.HTTP_200_OK, data={'msg': 'data deleted'})
