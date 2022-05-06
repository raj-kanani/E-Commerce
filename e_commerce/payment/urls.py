from django.urls import path
from . import views

urlpatterns = [
    # payment
    path('landing/', views.ProductLanding.as_view()),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSession.as_view(),
         name='create-checkout-session'),
    path('payment_success/', views.SuccessView.as_view()),
    path('payment_cancel/', views.CancelView.as_view()),
    path('mywebhook/', views.stripe_webhook),

]
