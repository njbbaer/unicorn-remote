
$(".dropdown-menu li a").click(function(){
  $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
  $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
});


$('#brightness').slider({
  formatter: function(value) {
    return value;
  }
});


$('.colors input[type=radio]').on('change', function() {
    console.log(this.value);
});