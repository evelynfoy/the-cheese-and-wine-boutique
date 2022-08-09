"""
Contains all the main views for the product application
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Cheese, Wine, Deal, Category
from .forms import ProductForm, CheeseForm, WineForm


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


@login_required
def add_product(request):
    """ Add product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        category_id = request.POST['category']
        category = get_object_or_404(Category, pk=category_id)
        if (form.is_valid()):
            product = form.save()
            if (category.name == 'cheese'):
                cheese = Cheese(product=product)
                cheese_form = CheeseForm(request.POST, request.FILES, instance=cheese)
                if (cheese_form.is_valid()):
                    cheese_form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[product.id]))
            elif (category.name == 'wine'):
                wine = Wine(product=product)
                wine_form = WineForm(request.POST, request.FILES, instance=wine)
                if (wine_form.is_valid()):
                    wine_form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. Please ensure the form is ' +
                           'valid.')
    else:
        form = ProductForm()
        cheese_form = CheeseForm()
        wine_form = WineForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'cheese_form': cheese_form,
        'wine_form': wine_form,
    }

    return render(request, template, context)
