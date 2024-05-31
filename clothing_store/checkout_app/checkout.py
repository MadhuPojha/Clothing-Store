from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Order(models.Model):
    #status options
    STATUS_PENDING = 'PENDING'
    STATUS_PROCESSING = 'PROCESSING'
    STATUS_SHIPPED = 'SHIPPED'
    STATUS_DELIVERED = 'DELIVERED'
    STATUS_CANCELED = 'CANCELED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_SHIPPED, 'Shipped'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELED, 'Canceled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_PENDING)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"Order total amount: {self.total_amount} | status: {self.status} | order date: {self.order_date}"

# Order Detail Model
class Order_Details(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"Order Contains {self.product.name}: {self.quantity}"