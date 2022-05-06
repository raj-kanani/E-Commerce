from django.db import models
from django.contrib.auth.models import User
from product.models import Product

ORDER_CHOICES = (
    ('Paid', 'Paid'),
    ('Unpaid', 'Unpaid')
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_choice = models.CharField(choices=ORDER_CHOICES, max_length=250)
    total = models.FloatField(blank=True)

    def _get_total(self):
        items = self.my_order.all()
        totals = 0
        for i in items:
            totals += i.total_price
        return totals

    total = property(_get_total)

    def __str__(self):
        return f"{self.user} - {self.order_choice} - {self.total}"


class OrderList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='my_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='my_order')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='my_order')
    price = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=120)

    def _get_total_price(self):
        return self.total_price

    total__price = property(_get_total_price)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.order.id}"
