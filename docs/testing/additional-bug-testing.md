## List of additional bugs or issues 


| Number | Bug | Status |  
|--------|---------|---------|
|  [#51](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/51)    |   Breaks site for administrator if they delete a product that is listed in their basket      | Closed  |  | 
|  [#56](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/56)    |   Layout of navbar for desktop logged out      |  Closed | 
|  [#57](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/57)    |   Subscribe button does not have sufficient contrast ratio     | Closed  | 
|  [#58](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/58)    |   HTML Validation Issue with font link     | Closed  | 
|  [#59](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/59)    |   Lighthouse Recommendations     | Open  | 
|  [#63](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/63)    |   Price and size font is too small on Product screen     |  Open | 
|  [#65](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/65)    |   Allows a negative price to be entered on Product Admin page      | Open  | 
|  [#66](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/66)    |   Image for August Deal is not displaying correctly in Success     |  Open | 
|  [#67](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/67)    |   Quantity field not displaying properly on Product Detail page     | Closed | 
|  [#68](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/68)    |   Dollar sign displaying instead of € on Shopping Basket page     | Closed  | 
|  [#69](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/69)    |   Back to Top link not appearing on home, product or basket page     |  Closed | 
|  [#70](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/70)    |   Insufficient contrast ratio on Checkout page     | Closed  | 
|  [#71](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/71)    |   Sign in button too small     | Closed  | 
|  [#72](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/72)    |   Checkbox is wrong color     | Open  | 
|  [#73](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/73)    |   Sign Out button is too small      | Closed  | 
|  [#74](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/74)    |   Change Update Product button on Product Detail to Save     | Open  | 
|  [#76](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/76)    |   Not found error when duplicate deal entered     | Open  | 
|  [#79](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/79)    |   Back to Profile button needs padding on right for phone/mobile     | Open  | 
|  [#80](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/80)    |   More padding required on Checkout success page for phone/mobile      |  Open  | 
|  [#96](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/96)    |   Back to Shop button incorrectly positioned on Order Confirmation     | Closed  | 
|  [#98](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/98)    |   Logout option not appearing when signed in     | Closed  | 

<br>

### Bug of note 
[#51](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/51)    |   Breaks site for administrator if they delete a product that is listed in their basket 

I noticed during my [SPIKE](https://github.com/evelynfoy/the-cheese-and-wine-boutique/issues/42) testing that if I deleted a product that was in my basket I got an [error](/docs/testing/images/bug-51-error.png) and the site did not work until I [cleared the site cookie](//docs/testing/images/bug-51-clear-cookie.png) from my browser.

I fixed the issue by inserting some [code](//docs/testing/images/bug-51-fix.png) into the basket_contents view in contexts.py which checks if each product exists on the database.    
It puts each item into a missing items array so they can be removed from the basket in the request session.

The error is no longer occuring and the issue is closed.


<br>

### Additional Issues
There are two more issues I have noticed since creating the above list.
1) If you logout you need to reresh the screen before the dropdown menu will allow you select the login option.
2) The dismiss button for the info alert displayed on editing a product is not working. Working ok on the success message.
3) If you delete a product that has been added to a deal product it will cause an error when you try to display that deal.     
   Currently the product needs to deleted from the admin menu.
