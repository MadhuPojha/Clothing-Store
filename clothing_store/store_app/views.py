from django.shortcuts import render
from store_app.models import Product, Product_Stock, Category
from datetime import datetime

# Create your views here.

def home(request):
    current_year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})


def product(request):
    product_list=Product.objects.all()
    product_dict={'product_item':product_list}
    return render(request,'product.html',context=product_dict)   # 'store_app/product.html'
    	

def product_stock(request):
    product_stock = Product_Stock.objects.all()
    return render(request, 'product_stock.html', {'product_stock': product_stock})	# 'store_app/product_stock.html'

def category(request):
    categorys = Category.objects.all()
    return render(request, 'category.html', {'category': category})	# 'store_app/category.html'


def cart(request):
    return render(request, "cart.html", {'cart': cart})

def order_confirmation(request):
    return render(request, 'order_confirmation.html', {'order_confirmation': order_confirmation})

def return_policy(request):
    return render(request, 'return_policy.html', {'return_policy': return_policy})

def contact_us(request):
    return render(request, 'contact_us.html', {'contact_us': contact_us})

def customer_service(request):
    return render(request, 'customer_service.html', {'customer_service': customer_service})


