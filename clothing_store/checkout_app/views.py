from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart_app.cart import Cart
from user_app.forms import UserPaymentInfoForm
from decimal import Decimal
from .models import Order

@login_required
def checkout(request):
    cart = Cart(request)
    sub_total_price = cart.get_sub_total_price()
    tax_percentage = Decimal('0.25') #25% tax
    tax_amount = round(sub_total_price * tax_percentage, 2)
    sub_total_with_tax = sub_total_price + tax_amount
    #calculate delivery cost
    if sub_total_price < 500:
        delivery_cost = Decimal('59.00')
    else:
        delivery_cost = Decimal('0.00')
    order_total = sub_total_with_tax + delivery_cost

    payment_form, payment_errors = payment_context(request)

    context = {
        'cart': cart,
        'sub_total_price': sub_total_price,
        'sub_total_with_tax': sub_total_with_tax,
        'tax_percentage': tax_percentage * 100,
        'tax_amount': tax_amount,
        'delivery_cost': delivery_cost,
        'order_total': order_total,
        'payment_form': payment_form,
        'payment_errors': payment_errors
    }
    return render(request, 'checkout.html', context)

@login_required
def payment_context(request):
    if request.method == "POST":
        payment_form = UserPaymentInfoForm(data=request.POST)
        if payment_form.is_valid():
            payment_info = payment_form.save(commit=False)
            payment_info.user = request.user
            payment_info.save()
            return payment_form, None
        else:
            print(payment_form.errors)
            return payment_form, payment_form.errors
    else:
        payment_form = UserPaymentInfoForm()
        return payment_form, None

@login_required
def order_summary(request):
    # Logic to display order summary and handle billing information
    if request.method == "POST":
        # Handle billing form submission
        pass
    return render(request, 'order_summary.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})