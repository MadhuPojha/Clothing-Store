from django.shortcuts import render
from store_app import Product, Product_Stock, Category

# Create your views here.
def product(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'product': product})	# 'store_app/product.html'

def product_stock(request):
    product_stock = Product_Stock.objects.all()
    return render(request, 'product_stock.html', {'product_stock': product_stock})	# 'store_app/product_stock.html'

def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})	# 'store_app/category.html'
