var AnimationProvider = (function () {
  var self;
  var animationProvider = function () {
    self = this;
  };

  animationProvider.prototype.getAnimations = function() {
    return self.animations;
  }

  animationProvider.prototype.animate = function (name, ...args) {
    return self[name].apply(self, args);
  };

  return animationProvider;
})();
