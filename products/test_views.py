"""
    Contains all the tests views for the products application
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product, Cheese, Wine, Deal


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

    def test_product_detail_wine_view(self):
        """
            Tests rendering of Product Detail view for a wine product.
            First creates a test category with a set value of 'Wine'.
            Then creates a test wine product with specific values.
            Then checks that a status of 200 is received on requesting the
            Product Detail template passing in the product for this product
        """
        category = Category.objects.create(name='wine',
                                           friendly_name='Wine')
        product = Product.objects.create(category=category,
                                         sku=1,
                                         name='MERLOT MOULIN DE GASSAC',
                                         description="Ripe fruit and spices.",
                                         price=15.75,
                                         size='75cl')
        Wine.objects.create(product=product,
                            origin='French',
                            production_method='Sustainable',
                            grape='Merlot',
                            wine_type='red')
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_deal_view(self):
        """
            Tests rendering of Product Detail view for a deal product.
            First creates a test category with a set value of 'Wine'.
            Then creates a test wine product with specific values.
            Then creates a test category with a set value of 'Cheese'.
            Then creates a test cheese product with specific values.
            Then creates a test deal product with specific values.
            Then checks that a status of 200 is received on requesting the
            Product Detail template passing in the product for this deal
        """
        category_wine = Category.objects.create(name='wine',
                                                friendly_name='Wine')
        product_wine = Product.objects.create(category=category_wine,
                                              sku=1,
                                              name='MERLOT MOULIN DE GASSAC',
                                              description="A wine.",
                                              price=15.75,
                                              size='75cl')
        category_cheese = Category.objects.create(name='cheese',
                                                  friendly_name='Cheese')
        product_cheese = Product.objects.create(category=category_cheese,
                                                sku=1,
                                                name='CAVANBERT',
                                                description="A cheese.",
                                                price=8,
                                                size='230G')
        category_deal = Category.objects.create(name='deal',
                                                friendly_name='Deal')
        product_deal = Product.objects.create(category=category_deal,
                                              sku=1,
                                              name='August Deal',
                                              description="Wine and cheese",
                                              price=30,
                                              size='230G and 75cl')
        Deal.objects.create(product=product_deal,
                            product1=product_cheese,
                            product2=product_wine)
        response = self.client.get(f'/products/{product_deal.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_add(self):
        """
            Tests rendering of 'products/add' url.
            Checks that a status of 200 is received on requesting this
            url.
        """
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)

    def test_product_add_template(self):
        """
            Tests templates rendered for 'products/add/' url.
            Checks that a status of 200 is received on requesting this
            url.
        """
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_product(self):
        """
            Tests that an product entry can be added using the 'product/add/
            url.
            Creates a test category with a set value of 'cheese'.
            Creates a test product.
            Creates a user.
            Logs on as this user.
            Then checks that a status of 200 is received on requesting the
            post function for the 'product/add/' url passing an object with
            product details for the test product.
        """
        category = Category.objects.create(name='cheese',
                                           friendly_name='Cheese')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post('/products/add/',
                                    {'category': category.id,
                                     'sku': ['1'],
                                     'name': 'CAVANBERT',
                                     'description': "A mild soft cheese.",
                                     'price': [8.00],
                                     'size': ['230G'],
                                     'milk': ['cow'],
                                     'region': ['Ireland'],
                                     'rennet': ['vegetarian'],
                                     'cheese_type': ['soft'],
                                     'age': ['4-10 weeks']
                                     })
        self.assertRedirects(response, '/products/1/')

    def test_can_add_wine_product(self):
        """
            Tests that a wine product entry can be added using the
            'product/add/ url.
            Creates a test category with a set value of 'wine'.
            Creates a test product.
            Creates a user.
            Logs on as this user.
            Then checks that a status of 200 is received on requesting the
            post function for the 'product/add/' url passing an object with
            product details for the test product.
        """
        category = Category.objects.create(name='wine',
                                           friendly_name='Wine')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post('/products/add/',
                                    {'category': category.id,
                                     'sku': ['1'],
                                     'name': 'CAVANBERT',
                                     'description': "A mild soft cheese.",
                                     'price': [8.00],
                                     'size': ['230G'],
                                     'origin': 'French',
                                     'production_method': 'Sustainable',
                                     'grape': 'Merlot',
                                     'wine_type': 'red',
                                     })
        self.assertRedirects(response, '/products/1/')

    def test_can_add_deal_product(self):
        """
            Tests that a deal product entry can be added using the
            'product/add/ url.
            Creates three test categories for cheese, wine and deal.
            Creates a test cheese product and a test wine product.
            Creates a superuser.
            Logs on as this user.
            Then checks that a status of 200 is received on requesting the
            post function for the 'product/add/' url passing an object with
            product details for the test product.
        """
        category_cheese = Category.objects.create(name='cheese',
                                                  friendly_name='Cheese')
        category_wine = Category.objects.create(name='wine',
                                                friendly_name='Wine')
        category_deal = Category.objects.create(name='deal',
                                                friendly_name='Deal')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        product_cheese = Product.objects.create(category=category_cheese,
                                                sku=1,
                                                name='MERLOT MOULIN DE GASSAC',
                                                description="Ripe fruit",
                                                price=15.75,
                                                size='75cl')
        product_wine = Product.objects.create(category=category_wine,
                                              sku=1,
                                              name='MERLOT MOULIN DE GASSAC',
                                              description="Ripe fruit",
                                              price=15.75,
                                              size='75cl')
        response = self.client.post('/products/add/',
                                    {'category': category_deal.id,
                                     'sku': ['1'],
                                     'name': 'CAVANBERT',
                                     'description': "A mild soft cheese.",
                                     'price': [8.00],
                                     'size': ['230G'],
                                     'product1': product_cheese.id,
                                     'product2': product_wine.id
                                     })
        self.assertRedirects(response, '/products/3/')


    def test_product_edit(self):
        """
            Tests rendering of 'products/edit' url.
            Creates a test category with a set value of 'cheese'.
            Creates a test product.
            Creates a superuser.
            Logs on as this user.
            Then checks that a status of 200 is received on requesting the
            post function for the 'product/edit/' url passing an object with
            product details for the test product.
            Then checks that a status of 200 is received on requesting this
            url passing the product id of the test product.
        """
        category_cheese = Category.objects.create(name='cheese',
                                                  friendly_name='Cheese')
        product = Product.objects.create(category=category_cheese,
                                         sku=1,
                                         name='Test Cheese',
                                         description="Cheesy",
                                         price=5.75,
                                         size='250g')
        cheese = Cheese.objects.create(product=product,
                                       milk='cow',
                                       region='Ireland',
                                       rennet='vegetarian',
                                       cheese_type='soft',
                                       age='4-10 weeks')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_edit_template(self):
        """
            Tests templates rendered for '/edit/<int:product_id>' url.
            Creates a test category with a set value of 'cheese'.
            Creates a test product.
            Creates a superuser.
            Logs on as this user.
            Then checks the templates used on requesting this
            url passing the product.id of the product.
        """
        category_cheese = Category.objects.create(name='cheese',
                                                  friendly_name='Cheese')
        product_cheese = Product.objects.create(category=category_cheese,
                                                sku=1,
                                                name='Test Cheese',
                                                description="Cheesy",
                                                price=5.75,
                                                size='250g')
        cheese = Cheese.objects.create(product=product_cheese,
                                       milk='cow',
                                       region='Ireland',
                                       rennet='vegetarian',
                                       cheese_type='soft',
                                       age='4-10 weeks')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get('/products/edit/1/')
        self.assertTemplateUsed(response, 'products/edit_product.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_edit_product(self):
        """
            Tests that an product entry can be edited using the 'product/edit/'
            url.
            Creates a test category with a set value of 'Cheese'.
            Creates a test product.
            Creates a test user.
            Logs on as this user.
            Then it requests the 'product/edit/' url passing in the id for the
            test product and an object containing test change details (description=
            'A mild soft cheese.').
            Then it checks that the response is redirection to the 'products/'
            url.
            Then the test product is retrieved from the database and tested to
            see if the value for description is in fact now equal to ''A mild soft cheese.'.
        """
        category = Category.objects.create(name='cheese',
                                           friendly_name='Cheese')
        product = Product.objects.create(category=category,
                                         sku=1,
                                         name='Test Cheese',
                                         description="Cheesy",
                                         price=5.75,
                                         size='250g')
        cheese = Cheese.objects.create(product=product,
                                       milk='cow',
                                       region='Ireland',
                                       rennet='vegetarian',
                                       cheese_type='soft',
                                       age='4-10 weeks')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy',
                                        is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post(f'/products/edit/{product.id}/',
                                    {'category': category.id,
                                     'sku': ['1'],
                                     'name': 'CAVANBERT',
                                     'description': "A mild soft cheese.",
                                     'price': [8.00],
                                     'size': ['230G'],
                                     'milk': ['cow'],
                                     'region': ['Ireland'],
                                     'rennet': ['vegetarian'],
                                     'cheese_type': ['soft'],
                                     'age': ['4-10 weeks'],
                                     })
        self.assertRedirects(response, '/products/1/')
        updated_product = Product.objects.get(sku=product.sku)
        self.assertEqual(updated_product.description, 'A mild soft cheese.')
