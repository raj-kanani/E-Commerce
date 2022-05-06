from django.urls import path
from . import views

urlpatterns = [
    path('address-create/', views.AddressCreate.as_view(), name='create'),
    path('address-list/', views.AddressList.as_view(), name='list'),
    path('addresss-update/<int:pk>/', views.AddresssUpdate.as_view(), name='up-del'),
]
