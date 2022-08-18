/* 
    On load 
        1) Show the correct div based on the category selected 
        2) Set the right required field based on the category selected   
*/ 

$(document).ready(function() {
    
    var category = $('#id_category').val();
    if (category == 1) {
        $('#cheeseDiv').show();
        $('#wineDiv').hide();
        $('#dealDiv').hide();
        $('#id_wine_type').attr('required', false);
    }
    else if (category == 2) {
        $('#wineDiv').show();
        $('#cheeseDiv').hide();
        $('#dealDiv').hide();
        $('#id_cheese_type').attr('required', false);
    }
    else if (category == 3) {
        $('#dealDiv').show();
        $('#cheeseDiv').hide();
        $('#wineDiv').hide();
        $('#id_cheese_type').attr('required', false);
        $('#id_wine_type').attr('required', false);
    }
    
});

$('#id_category').change(categoryChanged);

$('#sort-selector').change(sortChanged);

function categoryChanged() {
    var category = $(this).find('option:selected').text();
    if (category == 'Cheese') {
        $('#cheeseDiv').show();
        $('#wineDiv').hide();
        $('#dealDiv').hide();
        $('#id_wine_type').attr('required', false);
        $('#id_cheese_type').attr('required', true);

    }
    else if (category == 'Wine') {
        $('#cheeseDiv').hide();
        $('#wineDiv').show();
        $('#dealDiv').hide();
        $('#id_wine_type').attr('required', true);
        $('#id_cheese_type').attr('required', false);
    }
    else {
        $('#cheeseDiv').hide();
        $('#wineDiv').hide();
        $('#dealDiv').show();
        $('#id_wine_type').attr('required', false);
        $('#id_cheese_type').attr('required', false);
    }
}

function sortChanged() {
    var selector = $(this);
    var currentURL = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentURL.searchParams.set("sort", sort);
        currentURL.searchParams.set("direction", direction);
        window.location.replace(currentURL);
    } else {
        currentURL.searchParams.delete("sort");
        currentURL.searchParams.delete("direction");

        window.location.replace(currentURL);
    }
}