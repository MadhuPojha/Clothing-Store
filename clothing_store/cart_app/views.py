from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.views.decorators.http import require_POST
from store_app.models import Product
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, override_quantity=False)
    return redirect('cart_app:cart_detail')

@require_POST
#remove all items of specific product
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_app:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})