from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    # Your checkout logic goes here
    return render(request, 'checkout_app/checkout.html')

@login_required
def order_summary(request):
    # Logic to display order summary and handle billing information
    if request.method == "POST":
        # Handle billing form submission
        pass
    return render(request, 'checkout_app/order_summary.html')
# Create your views here.
