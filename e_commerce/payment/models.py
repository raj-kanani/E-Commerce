from django.db import models
from django.contrib.auth.models import User
from order.models import Order

PAYMENT_STATUS = (
    ('Pass', 'Pass'),
    ('Fail', 'Fail')
)

PAYMENT_TYPES = (
    ('Stripe', 'Stripe'),
    ('COD', 'COD')
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.CharField(max_length=125)
    status = models.CharField(max_length=200, choices=PAYMENT_STATUS)
    payment_mode = models.CharField(max_length=150, choices=PAYMENT_TYPES)
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        o = Order.objects.get(id=self.order_id.id)
        self.price = Order.total
        return super().save()

