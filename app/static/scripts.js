$('.dropdown-menu li a').click(function(){
    $(this).parents('.dropdown').find('.btn').html($(this).text() + ' <span class="caret"></span>');
    $(this).parents('.dropdown').find('.btn').val($(this).data('value'));
    $('#start-button').prop('disabled', false);
});

$('#brightness-slider').slider({
    formatter: function(value) {
        return value;
    }
});

$('#start-button').click(function(e) {
    var program = $('#programs-dropdown').val()
    var brightness = $('#brightness-slider').val()
    var rotation = $('input[name=rotation]:checked').val()
    $.ajax({
        type: "PUT",
        url: window.location.origin+'/api/program',
        success: function(resultData){
          console.log("Program started");
        },
    });
});

$('#stop-button').click(function(e) {
    $.ajax({
        type: "DELETE",
        url: window.location.origin+'/api/program',
        success: function(resultData){
          console.log("Program stopped");
        },
    });
});