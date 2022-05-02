import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import status

from .serializers import *
import logging
from .models import Payment
from rest_framework.response import Response

from order.models import Order


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ProductLanding(TemplateView):
    template_name = 'landing.html'

    def get(self, request):
        product = Payment.objects.all()
        serializer = PaymentSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        order = Order.objects.get(pk=data['order_id'])
        YOUR_DOMAIN = 'http://127.0.0.1;8000/'
        if Payment.objects.filter(order_id=order).exists():
            return Response({'msg': 'your payment already done'})
        else:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {

                        'price_data': {'currency': 'inr',
                                       'unit_amount': int(order.total_amount),
                                       'product_data': {'name': order.user.username}},

                        'quantity': 1,
                    },
                ],
                metadata={"order_id": order.id},
                mode='payment',
                success_url=YOUR_DOMAIN + 'payment_success',
                cancel_url=YOUR_DOMAIN + 'payment_cancel',
            )
            pay = Payment.objects.create(user=request.user,
                                         payment_mode=data['payment_mode'],
                                         order_id=order,
                                         status='Done')

            return JsonResponse({'url': checkout_session.url})


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
        '''
            Invalid Payment
        '''
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        '''
            Invalid signature
        '''
        return HttpResponse(status=400)
    logging.info("message 1 %s", event)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']['metadata']['order_id']
        pay = Payment.objects.get(order_id=session)
        if pay:
            pay.transaction_id = event['data']['object']['payment_intent']
            pay.save()
    return HttpResponse(status=status.HTTP_200_OK)
