from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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