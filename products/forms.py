"""
    Contains all the forms for the products application
"""
from django import forms
from .models import Product, Category, Cheese, Wine, Deal


class ProductForm(forms.ModelForm):
    """
        This form is for the basic core details that exist for all products
    """
    class Meta:
        """
            Includes all fields on the Product model
        """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
            Instantiates the form
            Loads the categories from the database into the dropdown and
            styles the text fields
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border=black rounded-0'


class CheeseForm(forms.ModelForm):
    """
        This form is for the cheese details that exist only for the cheese
        products
    """

    class Meta:
        """
            Includes all fields on the Cheese model
        """
        model = Cheese
        fields = ("cheese_type", "milk", "region", "rennet", "maker", "age")

    def __init__(self, *args, **kwargs):
        """
            Instantiates the form and styles the text fields
        """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border=black rounded-0'


class WineForm(forms.ModelForm):
    """
        This form is for the basic wine details that exist only for wine
        products
    """

    class Meta:
        """
            Includes all fields on the Wine model
        """
        model = Wine
        fields = ("wine_type", "origin", "grape", "production_method")

    def __init__(self, *args, **kwargs):
        """
            Instantiates the form and styles the text fields
        """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border=black rounded-0'


class DealForm(forms.ModelForm):
    """
        This form is for the basic deal details that exist only for deal
        products
    """

    class Meta:
        """
            Includes all fields on the Wine model
        """
        model = Deal
        fields = ("product1", "product2")

    def __init__(self, *args, **kwargs):
        """
            Instantiates the form and styles the text fields
        """
        super().__init__(*args, **kwargs)
        products = Product.objects.all()

        self.fields['product1'].choices = products
        self.fields['product2'].choices = products
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border=black rounded-0'
