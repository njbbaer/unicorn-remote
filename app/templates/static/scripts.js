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
    console.log($('#programs-dropdown').val())
    console.log($('#brightness-slider').val())
    console.log($('input[name=rotation]:checked').val())
});

$('#stop-button').click(function(e) {
    console.log('pressed stop button')
});