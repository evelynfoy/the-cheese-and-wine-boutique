"""
Contains all the main views for the product application
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Cheese, Wine, Deal, Category
from .forms import ProductForm, CheeseForm, WineForm, DealForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
                    messages.error(request,
                                   'Error adding product! ' +
                                   'Please check form details')
            elif category.name == 'wine':
                wine = Wine(product=product)
                wine_form = WineForm(request.POST, request.FILES,
                                     instance=wine)
                if wine_form.is_valid():
                    wine_form.save()
                    messages.success(request, 'Successfully added product!')
                    return redirect(reverse('product_detail',
                                            args=[product.id]))
                else:
                    messages.error(request,
                                   'Error adding product!' +
                                   'Please check form details')
            elif category.name == 'deal':
                deal = Deal(product=product)
                deal_form = DealForm(request.POST, request.FILES,
                                     instance=deal)
                if deal_form.is_valid():
                    deal_form.save()
                    messages.success(request, 'Successfully added product!')
                    return redirect(reverse('product_detail',
                                            args=[product.id]))
                else:
                    messages.error(request,
                                   'Error adding product!' +
                                   'Please check form details')
            else:
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail',
                                        args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. Please ensure the form ' +
                           'is valid.')
    else:
        form = ProductForm()
        cheese_form = CheeseForm()
        wine_form = WineForm()
        deal_form = DealForm()

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
    """
    Allows the store owner to edit product details.
    Only the relevant details are displayed for the product and category
    If entered details are valid the form is saved and a success message
    displayed
    and the user is returned to the product details page for the product
    otherwise an error message is displayed
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if product.category.name == 'cheese':
                cheese = get_object_or_404(Cheese, pk=product_id)
                cheese_form = CheeseForm(request.POST, request.FILES,
                                         instance=cheese)
                if cheese_form.is_valid():
                    form.save()
                    cheese_form.save()
                    messages.success(request, 'Successfully updated product!')
                    return redirect(reverse('product_detail',
                                            args=[product.id]))
                else:
                    message1 = 'Failed to update product.'
                    message2 = 'Please ensure the form is valid.'
                    messages.error(request, message1 + message2)

            elif product.category.name == 'wine':
                wine = get_object_or_404(Wine, pk=product_id)
                wine_form = WineForm(request.POST, request.FILES,
                                     instance=wine)
                if wine_form.is_valid():
                    form.save()
                    wine_form.save()
                    messages.success(request, 'Successfully updated product!')
                    return redirect(reverse('product_detail',
                                    args=[product.id]))
                else:
                    messages.error(request, 'Failed to update product. ' +
                                   'Please ensure the form is valid.')

            elif product.category.name == 'deal':
                deal = get_object_or_404(Deal, pk=product_id)
                deal_form = DealForm(request.POST, request.FILES,
                                     instance=deal)
                if deal_form.is_valid():
                    form.save()
                    deal_form.save()
                    messages.success(request, 'Successfully updated product!')
                    return redirect(reverse('product_detail',
                                            args=[product.id]))
                else:
                    messages.error(request, 'Failed to update product.' +
                                   'Please ensure the form is valid.')
            else:
                form.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('product_detail',
                                        args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure' +
                           'the form is valid.')
    else:
        form = ProductForm(instance=product)
        if product.category.name == 'cheese':
            cheese = get_object_or_404(Cheese, pk=product_id)
            cheese_form = CheeseForm(instance=cheese)
            wine_form = WineForm()
            deal_form = DealForm()
        elif product.category.name == 'wine':
            wine = get_object_or_404(Wine, pk=product_id)
            wine_form = WineForm(instance=wine)
            cheese_form = CheeseForm()
            deal_form = DealForm()
        else:
            deal = get_object_or_404(Deal, pk=product_id)
            deal_form = DealForm(instance=deal)
            cheese_form = CheeseForm()
            wine_form = WineForm()
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'cheese_form': cheese_form,
        'wine_form': wine_form,
        'deal_form': deal_form,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if product.category.name == 'cheese':
        cheese = get_object_or_404(Cheese, pk=product_id)
        cheese.delete()
    elif product.category.name == 'wine':
        wine = get_object_or_404(Wine, pk=product_id)
        wine.delete()
    elif product.category.name == 'deal':
        deal = get_object_or_404(Deal, pk=product_id)
        deal.delete()
    product.delete()
    messages.success(request, f'Product {product.name} deleted!')
    return redirect(reverse('products'))
