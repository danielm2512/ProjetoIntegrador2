"""Admin configurations for the Django app."""

from django.contrib import admin # "importação admin"
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, Product, Material, ProductMaterial, Order

class CustomUserAdmin(UserAdmin):
    """class representing a adminuser"""
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_inventory_admin',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(ProductMaterial)
admin.site.register(Order)
