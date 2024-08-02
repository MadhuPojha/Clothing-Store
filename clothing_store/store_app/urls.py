# Path: clothing_store/store_app/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'store_app'

urlpatterns = [
    path('', views.home, name='index'),
    path('items/<int:category_id>/', views.filter_items, name='filter_items'),
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('return_policy/', views.return_policy, name='return_policy'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path('customer_service/', views.customer_service, name='customer_service'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)