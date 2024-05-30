from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


# Product Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name  
     
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
        return f"Product: {self.Product.product} Size: {self.size} Color:{self.color} Stock:{self.stock}"
    
class ProductImages(models.Model):
    image = models.FileField(upload_to='products_images', blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)  # Relate images to products
    url = models.URLField(unique=True, max_length=300, blank=True)
    
    def __str__(self):
        return f"Image for {self.product.name}: {self.image.url}"

# TODO Remove unnecessary code
# class Order(models.Model):
#     #status options
#     STATUS_PENDING = 'PENDING'
#     STATUS_PROCESSING = 'PROCESSING'
#     STATUS_SHIPPED = 'SHIPPED'
#     STATUS_DELIVERED = 'DELIVERED'
#     STATUS_CANCELED = 'CANCELED'

#     STATUS_CHOICES = [
#         (STATUS_PENDING, 'Pending'),
#         (STATUS_PROCESSING, 'Processing'),
#         (STATUS_SHIPPED, 'Shipped'),
#         (STATUS_DELIVERED, 'Delivered'),
#         (STATUS_CANCELED, 'Canceled'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=20, decimal_places=2)
#     status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_PENDING)
#     order_date = models.DateTimeField(default=datetime.now, blank=True)
    
#     def __str__(self):
#         return f"Order total amount: {self.total_amount} | status: {self.status} | order date: {self.order_date}"

# # Order Detail Model
# class Order_Details(models.Model):
#     order=models.ForeignKey(Order,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField()
#     price=models.DecimalField(max_digits=6,decimal_places=2)

#     def __str__(self):
#         return f"Order Contains {self.product.name}: {self.quantity}"

#TODO Remove unnecessary code
# class Cart (models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     product = models.ManyToManyField(Product, through= 'CartItem') # need Product Class

#     def __str__(self):
#         return f"Cart for {self.user.username}"
    
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE) # need Product Class
#     quatity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"Quantity: {self.quatity} _ Product Name: {self.product.name}"

