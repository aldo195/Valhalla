(function() {
  'use strict';

  angular
    .module('app.search')
    .factory('searchService', searchService);

  /* @ngInject */
  function searchService($http, $log) {

    return {
      search: search,
      generate: generate
    };

    function search(data) {
      return $http.post('/api/search', data)
        .then(function (response) {
          return response.data;
        })
        .catch(function (error) {
          $log.error('XHR failed for search. ' + error.data);
        });
    }

    function generate(data) {
      return $http.post('/api/generate', data)
        .then(function (response) {
          return response.data;
        })
        .catch(function (error) {
          $log.error('XHR failed for create raid. ' + error.data);
        });
    }
  }

})();
