"""
Contains all the main views for the product application
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Cheese, Wine, Deal, Category
from .forms import ProductForm, CheeseForm, WineForm, DealForm


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
        if form.is_valid():
            product = form.save()
            if category.name == 'cheese':
                cheese = Cheese(product=product)
                cheese_form = CheeseForm(request.POST, request.FILES,
                                         instance=cheese)
                if cheese_form.is_valid():
                    cheese_form.save()
                    messages.success(request, 'Successfully added product!')
                    return redirect(reverse('product_detail',
                                            args=[product.id]))
                else:
                    messages.error(request, 'Error adding product! Please check form details')
            elif category.name == 'wine':
                wine = Wine(product=product)
                wine_form = WineForm(request.POST, request.FILES,
                                     instance=wine)
                if wine_form.is_valid():
                    wine_form.save()
                    messages.success(request, 'Successfully added product!')
                    return redirect(reverse('product_detail', args=[product.id]))
                else:
                    messages.error(request, 'Error adding product! Please check form details')
            elif category.name == 'deal':
                deal = Deal(product=product)
                deal_form = DealForm(request.POST, request.FILES,
                                     instance=deal)
                if deal_form.is_valid():
                    deal_form.save()
                    messages.success(request, 'Successfully added product!')
                    return redirect(reverse('product_detail', args=[product.id]))
                else:
                    messages.error(request, 'Error adding product! Please check form details')
        else:
            messages.error(request,
                           'Failed to add product. Please ensure the form ' +
                           'is valid.')
    else:
        form = ProductForm()
        cheese_form = CheeseForm()
        wine_form = WineForm()
        deal_form = DealForm()
        print(request.method)

    template = 'products/add_product.html'
    context = {
        'form': form,
        'cheese_form': cheese_form,
        'wine_form': wine_form,
        'deal_form': deal_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if product.category.name == 'cheese':
        cheese = get_object_or_404(Cheese, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if product.category.name == 'cheese':
            cheese_form = CheeseForm(request.POST, request.FILES, instance=cheese)
        if form.is_valid() and cheese_form.is_valid():
            form.save()
            cheese_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        cheese_form = CheeseForm(instance=cheese)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'cheese_form': cheese_form,
    }
    return render(request, template, context)
