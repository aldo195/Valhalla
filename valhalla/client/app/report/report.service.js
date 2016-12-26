(function() {
  'use strict';

  angular
    .module('app.report')
    .factory('reportService', reportService);

  /* @ngInject */
  function reportService($http, $log) {

    return {
      generate: generate,
      finish: finish
    };

    function generate(data) {
      return $http.post('/api/generate', data)
        .then(function (response) {
          return response.data;
        })
        .catch(function (error) {
          $log.error('XHR failed for create raid. ' + error.data);
        });
    }

    function finish(data) {
      return $http.post('/api/finish', data)
        .then(function (response) {
          return response.data;
        })
        .catch(function (error) {
          $log.error('XHR failed for create raid. ' + error.data);
        });
    }
  }

})();
