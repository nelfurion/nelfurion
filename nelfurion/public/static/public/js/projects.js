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

    var overlayHeight = 0;
    var paddingTop = parseInt(overlay.css('padding-top').split('px')[0])
    var paddingBottom = parseInt(overlay.css('padding-bottom').split('px')[0])

    $.each(overlay.children(), function (index, child) {
      overlayHeight += $(child).outerHeight(true);
    });

    overlayHeight += paddingTop + paddingBottom;

    if (overlay.height() < overlayHeight) {
      overlay.addClass('scrollable');
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

    $(this).removeClass('scrollable');
});

$(document).scroll(function() {
  var projects = $('.project-project');
  var scrollY = $(this).scrollTop();
  var windowHeight = $(window).height();

  $.each(projects, function(index, project) {
    project = $(project);
    if (scrollY + windowHeight > project.offset().top) {
      project.css('visibility', 'visible');
      project.addClass('animated fadeInUp');
    }
  });
});
