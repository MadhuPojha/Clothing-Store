from django.db import models

# Create your models here.


class Product_Stock(models.Model):
    pass
    product = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product} {self.size} {self.stock}"