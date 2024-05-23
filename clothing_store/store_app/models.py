from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Product_Category) #need to add Product_Category model
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(max_length=300)
    cover_image = models.ImageField(upload_to='product/image')

    def __str__(self):
        return f"Category {self.category} Product: {self.name} | Price: {self.price}"