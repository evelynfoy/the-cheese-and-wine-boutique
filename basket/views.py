"""  Contains all views for the basket app """
from django.shortcuts import redirect, get_object_or_404, render, HttpResponse
from django.shortcuts import reverse
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """
    A view to return the basket contents page
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a quantity of the specified product to the shopping basket
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                         f'Updated {product.name} quantity ' +
                         f'to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """
    Remove the specified product from the basket
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except OSError as product_not_found:
        messages.error(request, f'Error removing item: {product_not_found}')
        return HttpResponse(status=500)


def adjust_basket(request, item_id):
    """
    Adjust the quantity in the basket for the item passed in to the number
    entered.
    """

    product = get_object_or_404(Product, pk=item_id)
    name = product.name
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request,
                         f'Updated {name} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
