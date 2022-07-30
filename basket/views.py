from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # size = request.POST.get('size')
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

    print(messages)
    request.session['basket'] = basket
    return redirect(redirect_url)
