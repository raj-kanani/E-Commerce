from django.http import HttpResponse
from django.shortcuts import render
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .tasks import *
from .models import *
from .serializers import *
from cart.models import Cart, CartItem


def order_mail(request):
    send_email_task.delay()
    return HttpResponse('order mail success..')


def user_mail_sent(request):
    user_mail.delay()
    return HttpResponse('user mail successs')


def send_mail_perticular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=5, minute=30)
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_task' + '18',
                                       task='order.tasks.user_mail')  # name must be unique
    # args=json.dumps(([2, 3])) #args in pass the tuple in array value 2,3
    return HttpResponse('perticular task done')


class OrderApply(APIView):
    def get(self, request):
        o = Order.objects.all()
        serializer = OrderSerializer(o, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = request.data
        c = Cart.objects.get(user=request.user)
        c_item = CartItem.objects.filter(cart=c)
        if c_item:
            data = Order(user=user, order_choice=data['order_choice'])
            data.save()
        else:
            return Response({'msg': 'if you add product in cart'})

        for item in c_item:
            OrderList.objects.create(user=request.user, product=item.product, order=item.order, price=item.price,
                                     total_price=item.total_price)

        # return Response({'order_id': Order.id, })

        return Response({"order_id": Order.id, "order_amount": Order.total_amount,
                         "order_status": Order.order_status})
