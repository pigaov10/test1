from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateTimeField('created')

    def __str__(self):
        return self.name


class Delivery(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    lat = models.CharField(max_length=45)
    lon = models.CharField(max_length=45)
