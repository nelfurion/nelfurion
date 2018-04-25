/* off-canvas sidebar toggle */
$('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
    $('.collapse').toggleClass('in').toggleClass('hidden-xs').toggleClass('visible-xs');
});

$('#sidebar-toggle').on('click', function(event) {
  event.preventDefault();

  var links = $('.sidebar-link');
  var interval_step = 200;

  if ($('.sidebar-menu').css('display') == 'none') {
    $('.sidebar-menu').css('display', 'block');
    $('.sidebar-collapse').css('display', 'none');

    $('#main').removeClass('col-xs-12 col-sm-12 col-md-12 col-lg-11 col-xl-11');
    $('#main').addClass('col-xs-12 col-sm-12 col-md-12 col-lg-10 col-xl-10');

    $('.sidebar-container').removeClass('col-xs-12 col-sm-12 col-md-12 col-lg-1 col-xl-1');
    $('.sidebar-container').addClass('col-xs-12 col-sm-12 col-md-12 col-lg-2 col-xl-2');

    var interval = 0;
    $.each(links, function (index, link) {
      setTimeout(function () {
        $(link).removeClass('animated fadeOutLeft');
        $(link).css('display', 'block');
        $(link).addClass('animated rollIn');
      }, interval);

      interval += interval_step;
    });

    /*$( ".sidebar-link" ).animate({
      fontSize: '24px',
    }, 5000, function() {
      // Animation complete.
    });*/

  } else {
    var interval = 0;
    $.each(links, function (index, link) {
      setTimeout(function () {
        $(link).removeClass('animated rollIn');
        $(link).addClass('animated fadeOutLeft');
      }, interval);

      interval += interval_step / 2;
    });

    setTimeout(function() {
      $.each(links, function (index, link) {
        $(link).css('display', 'none');
      });

      $('.sidebar-menu').css('display', 'none');
      $('.sidebar-collapse').css('display', 'block');

      $('#main').removeClass('col-xs-10 col-sm-10 col-md-10 col-lg-10 col-xl-10');
      $('#main').addClass('col-xs-11 col-sm-11 col-md-11 col-lg-11 col-xl-11');

      $('.sidebar-container').removeClass('col-xs-2 col-sm-2 col-md-2 col-lg-2 col-xl-2');
      $('.sidebar-container').addClass('col-xs-1 col-sm-1 col-md-1 col-lg-1 col-xl-1');
    }, links.length * interval_step)
  }
});
