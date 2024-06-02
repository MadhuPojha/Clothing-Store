from django.shortcuts import render, get_object_or_404, redirect
from store_app.models import Product, Product_Stock, Category, ProductImages
from datetime import datetime
from cart_app.cart import Cart
from django.urls import reverse

def home(request):
    current_year = datetime.now().year
    items_view = Product.objects.all()
    return render(request, 'index.html', {'current_year': current_year,
                                          'items_view': items_view})
def product(request):
    sort_by = request.GET.get('sort_by', 'name')
    order = request.GET.get('order', 'asc')
    ordering = sort_by if order == 'asc' else f'-{sort_by}'
    
    product_list=Product.objects.all().order_by(ordering)
    product_dict={'product_item':product_list}
    
    #products = Product.objects.all().order_by(ordering)
    return render(request,'product.html',context=product_dict)   # 'store_app/product.html'	

def product_stock(request):
    product_stock = Product_Stock.objects.all()
    return render(request, 'product_stock.html', {'product_stock': product_stock})	# 'store_app/product_stock.html'

def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})

def product_details(request, product_id):
    product_detail = get_object_or_404(Product, id=product_id)
    product_stock = Product_Stock.objects.filter(product=product_detail)
    product_img = ProductImages.objects.filter(product=product_detail)

    product = {
        'product_detail': product_detail,
        'product_stock': product_stock,
        'product_img': product_img
    }
    return render(request, 'product_details.html', {'product': product})

def product_details(request, product_id):
    product_detail = get_object_or_404(Product, id=product_id)
    product_stock = Product_Stock.objects.filter(product=product_detail)
    product_img = ProductImages.objects.filter(product=product_detail)

    product = {
        'product_detail': product_detail,
        'product_stock': product_stock,
        'product_img': product_img
    }
    return render(request, 'product_details.html', {'product': product})

def order_confirmation(request):
    return render(request, 'order_confirmation.html', {'order_confirmation': order_confirmation})

def return_policy(request):
    return render(request, 'return_policy.html', {'return_policy': return_policy})

def contact_us(request):
    return render(request, 'contact_us.html', {'contact_us': contact_us})

def customer_service(request):
    return render(request, 'customer_service.html', {'customer_service': customer_service})

def filter_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Product.objects.filter(category=category)
    categories = Category.objects.all()  
    context = {
        'category': category,
        'items': items,
        #'categories': categories  # Pass categories to the template
    }
    return render(request, 'category.html', context)
