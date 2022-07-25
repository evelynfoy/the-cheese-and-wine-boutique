"""
    Contains all the tests views for the products application
"""
from django.test import TestCase
from .models import Category, Product


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
