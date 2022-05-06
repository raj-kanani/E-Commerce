import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import status
from .serializers import *
import logging
from .models import Payment
from rest_framework.response import Response
from product.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ProductLanding(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(product_name='realme')
        context = super(ProductLanding, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
        logging.info("message 1 %s", event)

    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    logging.info("message 1 %s", event)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']['metadata']['order_id']
        pay = Payment.objects.get(order_id=session)
        if pay:
            pay.transaction_id = event['data']['object']['payment_intent']
            pay.save()
    return HttpResponse(status=status.HTTP_200_OK)


class CreateCheckoutSession(View):
    def get(self, request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = Product.objects.get(pk=product_id)

        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {'currency': 'inr',
                                   'unit_amount': product.product_price,
                                   'product_data': {'name': product.product_name}},
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment_success',
            cancel_url=YOUR_DOMAIN + '/payment_cancel',
        )
        return JsonResponse({
            'pk': checkout_session.url
        })
