# Path: clothing_store/store_app/urls.py
from django.urls import path
from . import views


app_name = 'checkout_app'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('order-history/', views.order_history, name='order_history'),
    # path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
]