from django.db import models


# Create your models here.

class Product(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.product_name), filename])

    product_name = models.CharField(max_length=20, null=False, blank=True)
    description = models.TextField(max_length=50)
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to=nameFile, blank=True, null=True)

    def __str__(self):
        return self.product_name

    def get_display_price(self):
        return "{0:.2f}".format(self.product_price / 100)
