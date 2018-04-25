var GSAPAnimationProvider = (function (parent, Tween, $) {
  var self;
  var gsapAnimationProvider = function () {
    parent.call(this);
    this.tween = Tween;
    self = this;
  };

  gsapAnimationProvider.prototype = new parent();

  gsapAnimationProvider.prototype.scrollTo = function (toElement, options) {
    options = options || {};
    var animationOptions = $.extend({
      scrollTo: {y: offset}
    }, options);

    var offset= toElement.offset().top;

    return self.tween.to($(window), 1, animationOptions);
  };

  gsapAnimationProvider.prototype.slideLeft = function (element, fromPx, duration, options) {
    options = options || {};
    var animationOptions = $.extend({left: fromPx}, options);
    return self.tween.from(element, duration, animationOptions);
  };

  gsapAnimationProvider.prototype.slideRight = function (element, fromPx, duration, options) {
    options = options || {};
    var animationOptions = $.extend({right: fromPx}, options);
    return self.tween.from(element, duration, animationOptions);
  };

  gsapAnimationProvider.prototype.fadeIn = function (element, initialOpacity, duration, options) {
    options = options || {};
    var animationOptions = $.extend({opacity: initialOpacity}, options);
    return self.tween.from(element, duration, animationOptions);
  };

  gsapAnimationProvider.prototype.fadeOut = function (element, duration, options) {
    options = options || {};
    var animationOptions = $.extend({opacity: 0}, options);
    return self.tween.to(element, duration, animationOptions);
  };

  gsapAnimationProvider.prototype.enlarge = function (element, toWidth, toHeight, duration, options) {
    options = options || {};
    var animationOptions = $.extend({ width: toWidth, height: toHeight }, options);
    return self.tween.to(element, duration, animationOptions);
  };

  /* TODO: Extract new call animation function for this */
  function mergeJson() {

  }

  function organize(img, backgroundDivClass) {
    var imgParent = img.parent(),
      imgSrc = img.attr('src'),
      divClass = backgroundDivClass || 'img-panel';

    img.css('display', 'none');
    var tens = 0;
    for (var g=0; g<10; g++){
        imgParent.append('<div class="p' + g + ' ' + divClass + '"></div>');
        imgParent.find("." + divClass).eq(g).attr("style", "background-image:url("+imgSrc+"); width:10%; height:326px; background-position: "+tens+"% 0%;" );
        tens += 11;
    }

    return $('.' + divClass);
  }

  function randomNumber(min, max){
    return Math.floor(Math.random() * (1 + max - min) + min);
  }

  gsapAnimationProvider.prototype.backgroundStagger = function (image, backgroundDivClass) {
    var divClass = backgroundDivClass || 'img-panel',
      imgPanel = organize(image);

    function revert() {
      setTimeout(function () {
        console.log('donne');
        image.css('display', 'block');
        $('.' + divClass).css('display', 'none');

        //self.enlarge(image, 4, '100%', '326px');
      }, 1000);
    }

    self.tween.staggerFromTo(imgPanel, 2.5,
      {
        z:randomNumber(100, 500), rotation:randomNumber(360, 720), rotationX:randomNumber(-360, 360), rotationY:randomNumber(-360, 360), opacity:0
      }, {
        z:0, rotation:0, rotationX:0, rotationY:0, opacity: 1, transformOrigin:"50% 50% -1000", ease:Back.easeOut, easeParams:[.5],
        onComplete: revert
      },
      0.02
    );
  }

  return gsapAnimationProvider;
})(AnimationProvider, TweenMax, jQuery);
