## Automated Testing
Automated tests were created for the Products Application only due to time constraints.
There are a total of 18 tests - 5 for models and 13 for views -  [all tests pass](/docs/testing/images/automated-testing.png).

### Models
Models tested:
-   Category -  Tests the Category model by instantiating the model class and testing that the string function returns the correct value. 
-   Product -   Tests the Product model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of a test Category. 
-   Cheese  -   Tests the Cheese model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of both a test category and product. 
-   Wine    -   Tests the Wine model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of both a test category and product. 
-   Deal    -   Tests the Deal model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of both a test category and product. 

### Views
Views tested: 
-   all_products 
    1) Checks that a status of 200 is received on requesting the `/products/` page.
    2) Tests the templates rendered are `products/products.html` and `base.html`.
-   product_detail  
    1) Tests rendering of Product Detail view for a cheese product
    2) Tests rendering of Product Detail view for a wine product
    3) Tests rendering of Product Detail view for a deal product
-   add_product
    1) Tests that a product can be added.
    2) Tests the templates rendered are `products/add_product.html` and `base.html`.
-   can_add    
    1) Tests that a product can be added.
    2) Tests that a cheese product can be added.
    3) Tests that a wine product can be added.
    4) Tests that a deal product can be added.
-   edit_product
    1) Tests that a cheese product can be edited.
    2) Tests the templates rendered are `products/edit_product.html` and `base.html`.
-   can_edit
    1) Tests that a cheese product can be edited.
