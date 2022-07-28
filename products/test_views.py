"""
    Contains all the tests views for the products application
"""
from django.test import TestCase
from .models import Category, Product, Cheese


class TestViews(TestCase):
    """
        Test Class for all the tests
    """

    def test_product_list(self):
        """
            Tests rendering of product page or all_products view
            Checks that a status of 200 is received on requesting this page.
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_template(self):
        """
            Tests templates rendered for product page or all_products view.
        """
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_product_detail_cheese_view(self):
        """
            Tests rendering of Product Detail view for a cheese product.
            First creates a test category with a set value of 'Cheese'.
            Then creates a test cheese product with specific values.
            Then checks that a status of 200 is received on requesting the
            Product Detail template passing in the product  for this product
        """
        category = Category.objects.create(name='cheese',
                                           friendly_name='Cheese')
        product = Product.objects.create(category=category,
                                         sku=1,
                                         name='CAVANBERT',
                                         description="A mild soft cheese.",
                                         price=8,
                                         size='230G')
        Cheese.objects.create(product=product,
                              milk='cow',
                              region='Ireland',
                              rennet='vegetarian',
                              cheese_type='soft',
                              age='4-10 weeks')
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
