# Path: clothing_store/user_app/urls.py
from django.contrib import admin
from django.urls import path
from ..user_app import views

app_name = 'user_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    #path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),

]