from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart_app.cart import Cart

@login_required
def checkout(request):
    cart = Cart(request)
    sub_total_price = cart.get_sub_total_price()
    return render(request, 'checkout.html', {'cart': cart, 'sub_total_price': sub_total_price})

@login_required
def order_summary(request):
    # Logic to display order summary and handle billing information
    if request.method == "POST":
        # Handle billing form submission
        pass
    return render(request, 'order_summary.html')
# Create your views here.
