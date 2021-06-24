from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Item, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.product.name




    



