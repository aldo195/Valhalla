(function() {
  'use strict';

  angular
    .module('app.search', [])
    .constant('defaultTitle', 'An elegant title...')
    .controller('SearchController', SearchController);

  /* @ngInject */
  function SearchController($rootScope, $state, defaultTitle, searchService) {
    var searchVm = this;

    searchVm.title = defaultTitle;
    searchVm.selected = {};
    searchVm.malwarePath = "%appdata%"

    searchVm.targets = [
      {
        id: '101',
        name: 'An antivirus detection on a server'
      },
      {
        id: '102',
        name: 'DNS lookups to domains associated with a banking trojan every minute'
      },
      {
        id: '103',
        name: 'An end-user is blocked from accessing a malicious website'}
    ];

    searchVm.selectRaidType = function(){
      searchService.search({
        'q': searchVm.selected.target.id
      }).then(function(data) {
        //console.log(data);
      });
    };

    searchVm.createRaid = function(){
      console.log('Creating new raid with location ', searchVm.malwarePath);
      searchService.generate({
        'type': searchVm.selected.target.id,
        'path': searchVm.malwarePath
      }).then(function(data) {
        //console.log(data);
      });
    };

    searchVm.loadFromState = loadFromState;
    searchVm.search = search;

    // When the state changes, the controller will be updated and a search will take place.
    $rootScope.$on('$stateChangeSuccess', function () {
      searchVm.loadFromState();
    });

    // Load local variables from the state (the URL of the page).
    function loadFromState() {
      searchVm.searchTerm = $rootScope.$stateParams.term || 'sir';
      searchService.search({
        'q': searchVm.searchTerm
      }).then(function(data) {
        searchVm.searchResults = data;
      });
    }

    function search(term) {
      $state.go('search.term', {term: term});
    }

  }

})();
