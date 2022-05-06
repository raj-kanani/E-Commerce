from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('address.urls')),
    path('', include('cart.urls')),
    path('', include('order.urls')),
    path('', include('checkout.urls')),
    path('', include('product.urls')),
    path('', include('payment.urls')),
    path('', include('invoice.urls')),

]
