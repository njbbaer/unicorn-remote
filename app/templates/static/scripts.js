
// Programs dropwdown
$('.dropdown-menu li a').click(function(){
  $(this).parents('.dropdown').find('.btn').html($(this).text() + ' <span class="caret"></span>');
  $(this).parents('.dropdown').find('.btn').val($(this).data('value'));
  $('#start-button').prop('disabled', false);
});


// Brightness slider
$('#brightness').slider({
  formatter: function(value) {
    return value;
  }
});


// Rotation radio buttons
$('.colors input[type=radio]').on('change', function() {
    console.log(this.value);
});


// Click run button
$('#run-button').click(function(e) {
    console.log('Pressed run button')
});


// Click clear button
$('#stop-button').click(function(e) {
    console.log('pressed stop button')
});