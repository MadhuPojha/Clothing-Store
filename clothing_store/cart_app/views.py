from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from store_app.models import Product
from user_app.models import Address
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

def clear_cart(request):
    cart = Cart(request)
    cart.clear_all()
    return redirect('cart_app:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    item_count = len(cart)
    user_address = None
    # Fetch the user's address information
    if request.user.is_authenticated:
        user_address = Address.objects.filter(user=request.user).first()
    # Get the first name if the address exists
    first_name = user_address.first_name if user_address else "Guest"

    return render(request, 'cart.html', {'cart': cart,
                                        'item_count': item_count,
                                        'first_name':first_name,})