(function() {
  'use strict';

  angular
    .module('app.search')
    .factory('searchService', searchService);

  /* @ngInject */
  function searchService($http, $log) {

    return {
      generate: generate
    };

    function generate(data) {
      return $http.post('/api/generate', data)
        .then(function (response) {
          //console.log(response.data);
          return response.data;
        })
        .catch(function (error) {
          $log.error('XHR failed for create raid. ' + error.data);
        });
    }
  }

})();
