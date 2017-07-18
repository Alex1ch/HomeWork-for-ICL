var GraphView = angular.module("GraphView",['gridshore.c3js.chart']);


GraphView.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

GraphView.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});


GraphDraw.controller('GraphViewCtrl',function ($scope, $http) {
    $http({
            method: 'GET',
            url: $location.url(),
            headers: {
               'Content-Type': undefined
            },
            data:"Request ",
            transformRequest: angular.identity
        })
});