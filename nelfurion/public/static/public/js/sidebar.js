/* off-canvas sidebar toggle */
$('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
    $('.collapse').toggleClass('in').toggleClass('hidden-xs').toggleClass('visible-xs');
});

$('#sidebar-toggle').on('click', function(event) {
  event.preventDefault();
  if ($('.sidebar-menu').css('display') == 'none') {
    $('.sidebar-menu').css('display', 'block');
    $('.sidebar-collapse').css('display', 'none');

    $('#main').removeClass('col-xs-11 col-sm-11 col-md-11 col-lg-11');
    $('#main').addClass('col-xs-9 col-sm-9 col-md-9 col-lg-9');

    $('#sidebar').removeClass('col-xs-1 col-sm-1 col-md-1 col-lg-1');
    $('#sidebar').addClass('col-xs-3 col-sm-3 col-md-3 col-lg-3');

  } else {
    $('.sidebar-menu').css('display', 'none');
    $('.sidebar-collapse').css('display', 'block');

    $('#main').removeClass('col-xs-9 col-sm-9 col-md-9 col-lg-9');
    $('#main').addClass('col-xs-11 col-sm-11 col-md-11 col-lg-11');

    $('#sidebar').removeClass('col-xs-3 col-sm-3 col-md-3 col-lg-3');
    $('#sidebar').addClass('col-xs-1 col-sm-1 col-md-1 col-lg-1');
  }
});
