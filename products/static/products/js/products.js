function categoryChanged() {
    var category = $(this).find('option:selected').text();
    if (category == 'Cheese') {
        $(cheeseDiv).show();
    }
    else {
        $(cheeseDiv).hide();
    }
}

$(document).ready(function() {
    $('id_category').val(1);
    $('#cheeseDiv').show();
});

$('#id_category').change(categoryChanged);