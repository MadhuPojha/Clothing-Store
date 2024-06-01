from store_app.models import Product, ProductImages
from decimal import *
from django.conf import settings

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
     product_id = str(product.id)
     if product_id not in self.cart:
         self.cart[product_id] = {'quantity': 0,
                                  'price': str(product.price)}
     if override_quantity:
         self.cart[product_id]['quantity'] = quantity
     else:
         self.cart[product_id]['quantity'] += quantity
     self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                # If quantity is greater than 1, decrement the quantity by 1
                self.cart[product_id]['quantity'] -= 1
            else:
               del self.cart[product_id]
        self.save()

    # get the product objects and add them to the cart
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['image'] = product.images.first().image.url if product.images.exists() else None
        #add Product stock check
        #return structure containing product id and the other properties (Price,total_price and quantity.)
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    #output the number of items in the cart
    def __len__(self):
     return sum(item['quantity'] for item in self.cart.values())
    
    #output the subtotal price
    def get_sub_total_price(self):
     return sum(Decimal(item['price']) * item['quantity'] for item
                in self.cart.values())
    
    #Remove all items from the cart.
    def clear_all(self):
        # Use list() to create a copy of keys
        for key in list(self.cart.keys()):  
            del self.cart[key]
        self.save()

    def save(self):
       self.session[settings.CART_SESSION_ID] = self.cart
       self.session.modified = True