from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cart-crud', views.CartCRUD, basename='cart')

urlpatterns = [

    path('cart/', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('cart-createlist/', views.CartCreateList.as_view(), name='create-list'),
    path('cart-update/<int:pk>/', views.CartUpdateDelete.as_view(), name='update-delete'),

]
