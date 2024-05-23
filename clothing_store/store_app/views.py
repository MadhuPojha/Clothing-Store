from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    current_year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})

def login(request):
    return render(request, "login.html")

def category(request):
    return render(request, "category.html")

def cart(request):
    return render(request, "cart.html")

    
