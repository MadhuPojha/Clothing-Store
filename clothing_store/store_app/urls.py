# Path: clothing_store/store_app/urls.py
from django.urls import path
from . import views

app_name = 'store_app'

urlpatterns = [
    path('', views.home, name='index'),
    #path('login/', views.login, name='login'),
    path('category/', views.category, name='category'),
]