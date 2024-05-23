from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(on_delete=models.CASCADE) #need to add Product_Category model
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return f"Category {self.category} Product: {self.name} | Price: {self.price}"
    
class ProductImages(models.Model):
    image = models.FileField(upload_to='products_images', blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)  # Relate images to products
    url = models.URLField(unique=True, max_length=300, blank=True)
    
    def __str__(self):
        return f"Image for {self.product.name}: {self.image.url}"

class Cart (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through= 'CartItem') # need Product Class

    def __str__(self):
        return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # need Product Class
    quatity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Quantity: {self.quatity} _ Product Name: {self.product.name}"


