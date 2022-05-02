from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('payment_success/', views.SuccessView.as_view()),
    path('payment_cancel/', views.CancelView.as_view()),

]
