# Path: clothing_store/store_app/urls.py
from django.urls import path
from . import views

app_name = 'store_app'

urlpatterns = [
    path('', views.home, name='index'),
    #path('login/', views.login, name='login'),
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('return_policy/', views.return_policy, name='return_policy'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('customer_service/', views.customer_service, name='customer_service')
]