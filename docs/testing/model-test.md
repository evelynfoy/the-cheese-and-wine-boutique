Automated tests were created for the models in the Project App.
These models were 
-   Category -  Tests the Category model by instantiating the model class and testing that the string function returns the correct value. 
-   Product -   Tests the Product model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of a test Category. 
-   Cheese  -   Tests the Cheese model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of both a test category and product. 
-   Wine    -   Tests the Wine model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of both a test category and product. 
-   Deal    -   Tests the Deal model by instantiating the model class and testing that the string function returns the correct value.
                This requires the instantiating of both a test category and product. 

Example screenshots

Before the wine model was created the test produced this error

[No such table](/docs/testing/testwinemodelerr1.jpg)

[Test runs successfully](/docs/testing/testwinemodelerrafter.jpg)



