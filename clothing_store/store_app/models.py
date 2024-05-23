from django.db import models

# Create your models here.


class Product_Stock(models.Model):      #product_info 
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)

    def __str__(self):
        return f"Product: {self.Product.product} Size: {self.size} Color:{self.color} Stock:{self.stock}"