(function() {
  'use strict';

  angular
    .module('app.report', ['chart.js'])
    .controller('ReportController', ReportController);

  /* @ngInject */
  function ReportController() {
    var reportVm = this;

    reportVm.labels = ["January", "February", "March", "April", "May", "June", "July"];
    reportVm.series = ['Series A', 'Series B'];
    reportVm.data = [
        [65, 59, 80, 81, 560, 55, 40],
        [28, 48, 40, 19, 86, 27, 90]
    ];
    reportVm.datasetOverride = [{
        yAxisID: 'y-axis-1'
    }, {
        yAxisID: 'y-axis-2'
    }];
    reportVm.options = {
        scales: {
            yAxes: [{
                id: 'y-axis-1',
                type: 'linear',
                display: true,
                position: 'left'
            }, {
                id: 'y-axis-2',
                type: 'linear',
                display: true,
                position: 'right'
            }]
        }
    };
    reportVm.labels1 = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
    reportVm.series1 = ['Series A', 'Series B'];
    reportVm.data1 = [
        [65, 59, 80, 81, 56, 55, 40],
        [28, 48, 40, 19, 86, 27, 90]
    ];
  }
})();
