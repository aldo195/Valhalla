(function() {
  'use strict';

  angular
    .module('app.components')
    .directive('valhallaEnter', valhallaEnter);

  function valhallaEnter() {
    return {
      link: link,
      restrict: 'A'
    };

    function link(scope, element, attrs) {
      element.bind('keydown', function (e) {
        if (e.which === 13) {
          scope.$apply(function () {
            scope.$eval(attrs.valhallaEnter, {'e': e});
          });
          e.preventDefault();
        }
      });
    }

  }

})();
