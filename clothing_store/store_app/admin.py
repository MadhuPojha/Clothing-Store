from django.contrib import admin
from store_app.models import Product, ProductImages, Order, Category, Order_Details, Product_Stock
# Cart, CartItem

# admin.site.register(Cart)
# admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Order_Details)
admin.site.register(Product_Stock)
