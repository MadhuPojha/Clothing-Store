from django.contrib import admin
from store_app.models import Product, Cart, CartItem, ProductImages, Order

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Order)