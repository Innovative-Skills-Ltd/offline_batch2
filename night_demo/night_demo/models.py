from django.db import models

from django.db import models

class Product1(models.Model):
    name = models.CharField(max_length=100)       # Name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock = models.IntegerField(default=0)       # Quantity in stock
    created_at = models.DateTimeField(auto_now_add=True)