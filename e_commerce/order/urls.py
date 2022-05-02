from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('order-celery/', views.order_mail, name='order-celery'),
    path('user-mail/', views.user_mail_sent, name='user-mail'),
    path('perticular/', views.send_mail_perticular_time, name='perticular-mail'),
    path('order/', views.OrderApply.as_view())

]
