from django.contrib import admin
from store_app.models import Product, ProductImages, Category, Product_Stock

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(Product_Stock)
