(function() {
  'use strict';

  angular
    .module('app')
    .run(appRun);

  /* @ngInject */
  function appRun(routerHelper) {
    routerHelper.configureStates(getStates(), '/');
  }

  function getStates() {
    return [
      {
        state: 'hello',
        config: {
          url: '/',
          templateUrl: '/media/build/layout/hello.html'
        }
      },
      {
        state: 'raid',
        config: {
          url: '/raid',
          templateUrl: '/media/build/raid/raid.html',
          controller: 'RaidController as raidVm'
        }
      },
      {
        state: 'report',
        config: {
          url: '/report',
          templateUrl: '/media/build/report/report.html',
          controller: 'ReportController as reportVm'
        }
      }
    ];
  }

})();
