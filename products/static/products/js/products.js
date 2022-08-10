function categoryChanged() {
    var category = $(this).find('option:selected').text();
    if (category == 'Cheese') {
        $(cheeseDiv).show();
        $(wineDiv).hide();
        $(dealDiv).hide();
        $('#id_wine_type').attr('required', false);
        $('#id_cheese_type').attr('required', true);

    }
    else if (category == 'Wine') {
        $(cheeseDiv).hide();
        $(wineDiv).show();
        $(dealDiv).hide();
        $('#id_wine_type').attr('required', true);
        $('#id_cheese_type').attr('required', false);
    }
    else {
        $(cheeseDiv).hide();
        $(wineDiv).hide();
        $(dealDiv).show();
        $('#id_wine_type').attr('required', false);
        $('#id_cheese_type').attr('required', false);
    }
}

$(document).ready(function() {
    $('#id_category').val(1);
    $('#cheeseDiv').show();
    $('#wineDiv').hide();
    $('#dealDiv').hide();
    $('#id_wine_type').attr('required', false);
});

$('#id_category').change(categoryChanged);