from django.contrib import admin
from store_app.models import Product, Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)