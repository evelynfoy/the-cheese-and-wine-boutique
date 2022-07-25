"""
    Contains all the tests for the products application models
"""
from django.test import TestCase
from .models import Category, Product


class TestModels(TestCase):
    """
        Test Class for all the tests
    """

    def test_category_creation(self):
        """
            Tests creation of Category
            First creates a test category with a set value of 'cheese'
            Then tests that the str function on the created object returns the
            same value.
        """
        category = Category(name='cheese', friendly_name='Cheese')
        self.assertEqual(str(category), 'cheese')

    def test_product_creation(self):
        """
            Tests creation of a Product object.
            First creates a test category type with a set value of 'cheese'.
            Then creates a test product with specific values including
            the test product type and the name of 'CAVANBERT'.
            Then tests that the str function on the created object returns the
            name 'CAVANBERT'.
        """
        category = Category(name='cheese', friendly_name='Cheese')
        product = Product(category=category,
                          sku=1,
                          name='CAVANBERT',
                          description="A mild soft cheese.",
                          price=8,
                          size='230G')

        self.assertEqual(str(product), 'CAVANBERT')
