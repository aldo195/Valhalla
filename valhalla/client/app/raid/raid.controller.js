(function() {
  'use strict';

  angular
    .module('app.raid', [])
    .controller('RaidController', RaidController);

  /* @ngInject */
  function RaidController(raidService) {
    var raidVm = this;

    raidVm.selected = {};
    raidVm.trophy = '';
    raidVm.raidId = '';
    raidVm.elapsedTime = '0';

    raidVm.downloadURL = 'foobar';

    raidVm.targets = [
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

    raidVm.createRaid = createRaid;
    raidVm.finishRaid = finishRaid;

    function createRaid() {
      raidService.generate({
        'type': raidVm.selected.target.id
      }).then(function(data) {
        raidVm.raidId = data['raid_id'];
        var set_trophy = data['trophy'];  // Can't use the scope variable or the trophy entry field will be populated
        raidVm.raidType = data['raid_type'];
        raidVm.downloadURL = 'download_raid?type=' + raidVm.raidType + '&id=' + raidVm.raidId + '&trophy=' + set_trophy;
      });
    }

    function finishRaid() {
      raidService.finish({
        'raidId': raidVm.raidId,
        'trophy': raidVm.trophy
      }).then(function(data) {
        raidVm.elapsedTime = data;
      });
    }
  }
})();
