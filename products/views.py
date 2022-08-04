"""
Contains all the main views for the product application
"""
from django.shortcuts import render, get_object_or_404
from .models import Product, Cheese, Wine, Deal
from .forms import ProductForm, CheeseForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    if product.category.name == "cheese":
        cheese = get_object_or_404(Cheese, pk=product_id)
        context = {
            'product': product,
            'cheese': cheese,
        }
    elif product.category.name == "wine":
        wine = get_object_or_404(Wine, pk=product_id)
        context = {
            'product': product,
            'wine': wine,
        }
    elif product.category.name == "deal":
        deal = get_object_or_404(Deal, pk=product_id)
        context = {
            'product': product,
            'deal': deal,
        }
    else:
        context = {
            'product': product,
        }
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add product to the store """
    
    form = ProductForm(request.POST, request.FILES)
    cheese_form = CheeseForm(request.POST, request.FILES)
    template = 'products/add_product.html'
    context = {
        'form': form,
        'cheese_form': cheese_form,
    }

    return render(request, template, context)
