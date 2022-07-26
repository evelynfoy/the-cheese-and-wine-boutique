"""
    Registers all the models for the products application
"""
from django.contrib import admin
from .models import Product, Category, Cheese


class ProductAdmin(admin.ModelAdmin):
    """Product """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'size',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ Category """
    list_display = (
        'friendly_name',
        'name',
    )


class CheeseAdmin(admin.ModelAdmin):
    """Cheese """
    list_display = (
        'product',
        'cheese_type',
        'milk',
        'region',
        'rennet',
        'maker',
        'age',
    )

    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cheese, CheeseAdmin)
