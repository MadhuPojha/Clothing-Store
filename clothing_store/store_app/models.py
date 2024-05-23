from django.db import models

# Create your models here.

# Product Caterory Model
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.name

# Order Detail Model
class Order_Details(models.Model):
    order_detail_id= models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.order_detail_id