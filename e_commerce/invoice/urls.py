from django.urls import path, include
from . import views

urlpatterns = [

    path('pdf/', views.GenerateInvoice.as_view(), name='pdf'),
    path('pdf2/', views.DownloadInvoice.as_view(), name='pdf2'),
    path('pdf3/', views.ShareInvoice.as_view(), name='pdf3'),

]
