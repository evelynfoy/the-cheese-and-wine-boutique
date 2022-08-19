- Add a test for the view add_product but for a deal product
- Change settings to test database to test
- Add code to add product view for deal products
- Add deal form
- Add javascript code to remove required attribute from cheese-type and wine type when adding a deal product
- Add javascript to hide/show the deals div on selection of deal as category

Issues
- Product lists not set in form on instantiation
- User not set to super user to allow adding
- Products not created in test_view before post
- Category only created for deal not for cheese and wine also to allow creation of the products
- Products1 and 2 appearing with no labels 

Process 
- Used print statements to check if forms were valid and to find out what path in the code was being executed.
- Also to find out product ids of products created.

Issue Solution
-  Products1 and 2 appearing with no labels 
-   fields in this form were not defined as crispy
![Before Fix](/docs/testing/DealIssue2Before.jpg "Before Fix").
![Fix](/docs/testing/DealIssue2Fix.jpg "Fix").
![After Fix](/docs/testing/DealIssue2After.jpg "After Fix").

