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
    transaction_id = models.CharField(max_length=125)
    status = models.CharField(max_length=200, choices=PAYMENT_STATUS)
    payment_type = models.CharField(max_length=150, choices=PAYMENT_TYPES)
    payment_price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        order = Order.objects.get(id=self.order_id.id)
        self.payment_price = order.total
        return super().save()

