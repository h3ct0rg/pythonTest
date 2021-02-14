from django.db import models
from application.users.models import *
from model_utils.models import TimeStampedModel

# Create your models here.
class Brand(TimeStampedModel):
    name = models.CharField('Name',max_length=50)
    description = models.CharField('Description',max_length=200)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    sku = models.CharField('Sku',max_length=50)
    name = models.CharField('Name',max_length=50)
    price = models.FloatField('Price')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LogUpdateProduct(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LogSeeProduct(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dateView = models.DateTimeField('Date Review')

    def __str__(self):
        return self.product.name + " - " + self.dateView.strftime("%m/%d/%Y, %H:%M:%S")

