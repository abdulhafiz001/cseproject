import email
from itertools import product
from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.

class Destination:
    id : int
    name : str
    img : str
    desc : str
    price: int


# class Customer(models.Model):
#     name = models.CharField(max_length=255, )
#     email = models.CharField(max_length=200)


class Cars(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE )
    image = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    # quantity = models.IntegerField()

    def __str__(self):
        return self.brand + " " + self.name

# class Order(models.Model):
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

# class OrderItem():
#     quantity = models.IntegerField()
#     product = models.ForeignKey(Cars, on_delete=models.CASCADE)