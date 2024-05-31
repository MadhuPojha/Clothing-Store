from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


# Product Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"Name: {self.name} Id: {self.id} " 
     
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return f"Category {self.category} Product: {self.name} | Price: {self.price}"

class Product_Stock(models.Model):      #product_info 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)

    def __str__(self):
        return f"Product: {self.product} Size: {self.size} Color:{self.color} Stock:{self.stock}"
    
class ProductImages(models.Model):
    image = models.ImageField(upload_to='products_images', blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)  # Relate images to products
    #url = models.URLField(unique=True, max_length=300, blank=True)
    
    def __str__(self):
        return f"Image for {self.product.name}: {self.image.url}"
