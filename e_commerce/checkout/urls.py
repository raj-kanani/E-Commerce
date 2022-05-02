from django.urls import path
from . import views

urlpatterns = [

    path('checkout-create/', views.CheckoutCreate.as_view(), name='checkout-create'),
    path('checkout-list/', views.CheckoutList.as_view(), name='checkout-list'),

]
