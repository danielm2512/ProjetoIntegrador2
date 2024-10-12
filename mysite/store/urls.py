from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('manage_stock/', views.manage_stock, name='manage_stock'),
    path('filter_products/', views.filter_products, name='filter_products')
    ]