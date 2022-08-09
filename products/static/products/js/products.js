function categoryChanged() {
    var category = $(this).find('option:selected').text();
    if (category == 'Cheese') {
        $(cheeseDiv).show();
        $(wineDiv).hide();
        $('#id_wine_type').attr('required', false);
        $('#id_cheese_type').attr('required', true);

    }
    else {
        $(cheeseDiv).hide();
        $(wineDiv).show();
        $('#id_wine_type').attr('required', true);
        $('#id_cheese_type').attr('required', false);
    }
}

$(document).ready(function() {
    $('#id_category').val(1);
    $('#cheeseDiv').show();
    $('#wineDiv').hide();
    $('#id_wine_type').attr('required', false);
});

$('#id_category').change(categoryChanged);