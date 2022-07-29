"""
    Contains all the tests for the products application models
"""
from django.test import TestCase
from .models import Category, Product, Cheese, Wine, Deal


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

    def test_cheese_creation(self):
        """
            Tests creation of a cheese object.
            First creates a test category type with a set value of 'cheese'.
            Then creates a test product with specific values including
            the test product type and the name of 'CAVANBERT'.
            Then creates a test cheese with the product of 'CAVANBERT'
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
        cheese = Cheese(product=product,
                        milk='cow',
                        region='Ireland',
                        rennet='vegetarian',
                        cheese_type='soft',
                        age='4-10 weeks')

        self.assertEqual(str(cheese), 'CAVANBERT')

    def test_wine_creation(self):
        """
            Tests creation of a wine object.
            First creates a test category type with a set value of 'wine'.
            Then creates a test product with specific values including
            the test product type and the name of 'MERLOT MOULIN DE GASSAC'.
            Then creates a test cheese with the product of 'MERLOT MOULIN DE
            GASSAC'
            Then tests that the str function on the created object returns the
            name 'MERLOT MOULIN DE GASSAC'.
        """
        category = Category(name='wine', friendly_name='Wine')
        product = Product(category=category,
                          sku=1,
                          name='MERLOT MOULIN DE GASSAC',
                          description="Ripe fruit and spices.",
                          price=15.75,
                          size='75cl')
        wine = Wine(product=product,
                    origin='French',
                    production_method='Sustainable',
                    grape='Merlot',
                    wine_type='red')

        self.assertEqual(str(wine), 'MERLOT MOULIN DE GASSAC')

    def test_deal_creation(self):
        """
            Tests creation of a deal object.
            First creates two test category types for 'wine' and 'cheese'.
            Then creates a test wine product with the name of 'MERLOT MOULIN DE
            GASSAC'.
            Then creates a test cheese product with the name of 'CAVANBERT'.
            Then tests the creation of a deal product with the name 'Augusts
            Special'
            Then tests that the str function on the created object returns the
            name 'Augusts Special'.
        """
        category_cheese = Category(name='cheese', friendly_name='Cheese')
        product_cheese = Product(category=category_cheese,
                                 sku=1,
                                 name='CAVANBERT',
                                 description="A mild soft cheese.",
                                 price=8,
                                 size='230G')
        category_wine = Category(name='wine', friendly_name='Wine')
        product_wine = Product(category=category_wine,
                               sku=2,
                               name='MERLOT MOULIN DE GASSAC',
                               description="Ripe fruit and spices.",
                               price=15.75,
                               size='75cl')
        category_deal = Category(name='deal', friendly_name='Deal')
        product_deal = Product(category=category_deal,
                               sku=3,
                               name='August Deal',
                               description="Cheese and wine",
                               price=30,
                               size='75cl and 230g')
        deal = Deal(product=product_deal,
                    product1=product_wine,
                    product2=product_cheese)

        self.assertEqual(str(deal), 'August Deal')
