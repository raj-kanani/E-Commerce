from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('product-crud', views.ProductCRUD, basename='product')

urlpatterns = [
    path('product/', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest-framework')),

]
