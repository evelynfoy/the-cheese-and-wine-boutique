""" Contains Models for the products app
    Category
    Products
"""
from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
        This is a simple model used to distinguish diffent product types.
        Details held are just a name and a friendly name
    """
    class Meta:
        """ Plural name """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ Front end name in case names are unsuitable  """
        return self.friendly_name


class Product(models.Model):
    """
        This model holds the details of each product available to purchase.
        Fields held are :
            Name: CharField(max_length=200, unique=True),
            sku: CharField(max_length=200, unique=True),
            category: name from Category model,
            description: TextField,
            price: DecimalField(max_digits=6, decimal_places=2),
            size: CharField(max_length=200, unique=True),
            image: ImageField, defaults to placeholder,
            image_url: URLField(max_length=1024, null=True, blank=True)
        The str function returns the name of the product as a string.
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.name)


class Cheese(models.Model):
    """
        This model holds the cheese details for the cheese products available
        to purchase.
        Fields held are :
            milk: CharField(max_length=200),
            region: CharField(max_length=200),
            rennet: CharField(max_length=200),
            type: CharField(max_length=200),
        The str function returns the name of the product as a string.
    """
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
        )
    cheese_type = models.CharField(max_length=20)
    milk = models.CharField(max_length=20, null=True, blank=True)
    region = models.CharField(max_length=20, null=True, blank=True)
    rennet = models.CharField(max_length=20, null=True, blank=True)
    maker = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.product.name)
