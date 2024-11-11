# Arquivo models.py em mysite/store/

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    # perfil
    is_inventory_admin = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, null=True, blank=True)
    # produto características

class Material(models.Model):
    name = models.CharField(max_length=50)
    # material

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    # produto/material

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # pedido
class CustomUser(AbstractUser):
    # customer
    is_inventory_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )

class CartItem(models.Model):
    # item carrinho
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()