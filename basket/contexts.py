"""
Contains context for shopping basket
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """
    A context processor which reads through the basket items in the
    request session, calculates the number of items, total and delivery
    cost which it returns as a context making these details available to
    all templates.
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    missing_items = []
    for item_id, quantity in basket.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'line_total': product.price * quantity
            })
        except Exception:
            missing_items.append(item_id)

    if missing_items:
        for item_id in missing_items:
            basket = request.session.get('basket', {})
            basket.pop(item_id)
            request.session['basket'] = basket

    delivery = (total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE))/100

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context
