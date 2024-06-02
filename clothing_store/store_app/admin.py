from django.contrib import admin
from store_app.models import Product, ProductImages, Category, Product_Stock
from user_app.models import UserProfileInfo, UserPaymentInfo, Address, UserShippingInfo, UserBillingInfo

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(Product_Stock)
admin.site.register(UserProfileInfo)
admin.site.register(UserPaymentInfo)
admin.site.register(Address)
admin.site.register(UserShippingInfo)
admin.site.register(UserBillingInfo)
