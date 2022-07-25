"""
    Registers all the models for the products application
"""
from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
