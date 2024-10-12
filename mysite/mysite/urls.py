"""importacao"""
from django.urls import path, include
from store import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('manage_stock/', views.manage_stock, name='manage_stock'),
    path('filter_products/', views.filter_products, name='filter_products'),
    path('admin/', admin.site.urls),  # Esta linha inclui as URLs do admin
    path('', include('store.urls')),  # Esta linha inclui as URLs do app 'store'
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'    )
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)