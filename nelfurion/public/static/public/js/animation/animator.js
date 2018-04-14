var Animator = (function () {
  var self;
  function animator(animationProviders) {
    this.animationProviders = animationProviders;
    self = this;
  };

  animator.prototype.animate = function (animationName, ...args) {
    for (var i = 0; i < self.animationProviders.length; i++) {
      if (self.animationProviders[i][animationName]) {
        return self.animationProviders[i][animationName].apply(null, args);
      }
    };
  };

  return animator;
})();
