# store/forms.py
"""
Forms module for the store application.

This module contains form definitions used in the store application.
"""

from django import forms
from .models import Product, Profile, Material


class ProductForm(forms.ModelForm):
    """Form for creating and updating Product instances."""
    class Meta:
        """Form for creating and updating model instances."""
        model = Product
        fields = ['name', 'price']

class ProfileForm(forms.ModelForm):
    """Form for creating and updating profile instances."""
    class Meta:
        """Form for creating and updating fields - profile instances."""
        model = Profile
        fields = ['is_inventory_admin']

class MaterialForm(forms.ModelForm):
    """Form for creating and updating item instances."""
    class Meta:
        """Form for creating and updating characteristics instances."""
        model = Material
        fields =  ['name']
