"""Admin configurations for the Django app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from django.shortcuts import render
from django.db.models import Sum
from .models import CustomUser, Profile, Product, Material, ProductMaterial, Order, Sale
from django.db.models.functions import TruncDate
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

class CustomUserAdmin(UserAdmin):
    """class representing a adminuser"""
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_inventory_admin',)}),
    )

class SalesDashboardAdmin(admin.ModelAdmin):
    change_list_template = "admin/sales_list_with_dashboard.html" 

    def get_queryset(self, request):
        from django.db.models.functions import TruncDate
        from django.db.models import Sum
    
        queryset = super().get_queryset(request)
        return queryset.annotate(
            truncated_date=TruncDate('date'),
            annotated_total_price=Sum('total_price')
        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_site.admin_view(self.dashboard_view), name='sales-dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        sales = Sale.objects.annotate(truncated_date=TruncDate('date')).values('truncated_date').annotate(total_price=Sum('total_price'))
        sales_data = json.dumps(list(sales), cls=DjangoJSONEncoder)
        return render(request, "admin/sales_dashboard.html", {"sales_data": sales_data})


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(ProductMaterial)
admin.site.register(Order)
admin.site.register(Sale, SalesDashboardAdmin)
