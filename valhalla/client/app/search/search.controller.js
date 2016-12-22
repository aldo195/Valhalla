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
    searchVm.malwarePath = '%appdata%';

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

    searchVm.createRaid = function() {
      console.log('Creating new raid with location ', searchVm.malwarePath);
      searchService.generate({
        'type': searchVm.selected.target.id,
        'path': searchVm.malwarePath
      }).then(function(data) {
        console.log(data);
        searchVm.raidId = data;
      });
    };
  }

})();
