from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
from .settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_commerce.settings')
app = Celery('e_commerce')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
app.config_from_object(settings, namespace='CELERY')  # CELERY means all celery related configuration keys

# celery beat setting send mail every day for all users
app.conf.beat_schedule = {
    'send-mail-every-day-at-2': {
        'task': 'order.tasks.send_email_task',
        'schedule': crontab(hour=11, minute=10),
        # 'args' :(2,)
    }
}

# celery beat settings
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
