$('.project-card-img, .project-card-img-overlay').mouseenter(function(event) {
  var overlay = $(this).siblings('.project-card-img-overlay');
  var overlayParentHeight = overlay.parent().outerHeight();
  if (overlay.length > 0) {
    overlay.addClass('overlay-visible')
      .removeClass('overlay-invisible');

    var image = $(this).siblings('.project-card-img').filter(':not(.project-card-visible-background)');
    if ($(this).prop('tagName') == 'IMG') {
      image = $(this);
    }

    var cardVisibleBackgroundImage = $(this).siblings('.project-card-visible-background');
    if (cardVisibleBackgroundImage.length > 0) {
      image.css('display', 'none');
      cardVisibleBackgroundImage.css('display', 'block');
    }
  }
});

$('.project-card-img-overlay').mouseleave(function(event) {
  $(this).filter('.project-card-img-overlay')
    .removeClass('overlay-visible')
    .addClass('overlay-invisible');

    var image = $(this).siblings('.project-card-img');

    var cardVisibleBackgroundImage = $(this).siblings('.project-card-visible-background');

    if (cardVisibleBackgroundImage.length > 0) {
      image.css('display', 'block');
      cardVisibleBackgroundImage.css('display', 'none');
    }
});
