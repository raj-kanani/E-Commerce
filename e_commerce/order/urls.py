from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('order-celery/', views.order_mail, name='order-celery'),
    path('order/', views.OrderApply.as_view())

]
