## Automated Testing
Automated tests were created for the Products Application

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


Example screenshots

Before the wine model was created the test produced this error

[No such table](/docs/testing/testwinemodelerr1.jpg)

[Test runs successfully](/docs/testing/testwinemodelerrafter.jpg)



