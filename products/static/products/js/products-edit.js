/* Javascript for the edit product page 
   Checks the category of the product and displays the appropriate additional details div 
   hiding the others and the input field for the category field itself so it can't be changed */
   
$(document).ready(function() {
    
    var cat = $('#id_category').val();
    if (cat == 1) {
        $('#cheeseDiv').show();
        $('#wineDiv').hide();
        $('#dealDiv').hide();
        $('#id_wine_type').attr('required', false);
    }
    else if (cat == 2) {
        $('#wineDiv').show();
        $('#cheeseDiv').hide();
        $('#dealDiv').hide();
        $('#id_cheese_type').attr('required', false);
    }
    else if (cat == 3) {
        console.log(cat);
        $('#dealDiv').show();
        $('#cheeseDiv').hide();
        $('#wineDiv').hide();
        $('#id_cheese_type').attr('required', false);
        $('#id_wine_type').attr('required', false);
    }
    $('#div_id_category').hide();
    
});

