from time import sleep

from django.core.mail import send_mail
from e_commerce import settings
from celery import shared_task

from .models import *


@shared_task
def send_email_task():
    sleep(5)
    send_mail('Finally order confirm',
              'continue shopping now',
              'raj.kanani@plutustec.com',
              ['raj.kanani1487@gmail.com'],
              fail_silently=False
              )
    return None


@shared_task(bind=True)
def user_mail(self):
    orders = OrderList.objects.all()
    for order in orders:
        mail_subject = 'this is product order'
        message = 'confirm order'
        to_email = order.user
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True

        )
        return 'your mail success sent by tasks'
