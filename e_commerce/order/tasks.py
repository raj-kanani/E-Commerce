from time import sleep
from django.core.mail import send_mail
from celery import shared_task


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
