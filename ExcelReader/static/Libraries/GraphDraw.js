var GraphDraw = angular.module("GraphDraw",['gridshore.c3js.chart']);

GraphDraw.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

GraphDraw.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

GraphDraw.controller('GraphDrawCtrl',function ($scope, $http) {
    $scope.formModel = new FormData();


    var file = {};
        $scope.upload = function(fileInput) {
    file = fileInput.files[0];
    };
    $scope.datapoints=[];
    $scope.datacolumns=[];
    $scope.datax={"id":"x"};
    
    $scope.items = [];


    $http({
        method: 'GET',
        url: '/excelreader/getlist'
    }).then(function (response) {
        console.log(response.data);
        var entries=response.data.split('\n');
        for(i=0;i<response.data.split('\n').length-1;i++){
            var split=entries[i].split('/*/');
            $scope.items.push({name:split[2]+"    -    "+split[1],id:split[0]});
        }
    })



    $scope.SelectChange = function () {
        $http({
        method: 'GET',
        url: '/excelreader/getgraph/id='+$scope.selectedItem['id']
    }).then(function (response) {
        $scope.xdata=response.data.split('\n')[0].split(',');
        $scope.ydata=response.data.split('\n')[1].split(',');
        console.log($scope.xdata);
        console.log($scope.ydata);

        $scope.datapoints=[];

        for(i=0;i<$scope.xdata.length;i++){
            $scope.datapoints.push({"x":$scope.xdata[i],"y":parseFloat($scope.ydata[i])});
        }

        $scope.datacolumns=[{"id":"y","type":"spline", "color":"red"}];
        $scope.datax={"id":"x"};
    })
    };

    

    $scope.OnSubmit = function () {
        $scope.formModel.append('file',file);
        $scope.formModel.append('name',$scope.name);
        $scope.formModel.append('desc',$scope.desc);
        console.log("Submitting...");

        $http({
            method: 'POST',
            url: '/excelreader/loadfile/',
            headers: {
               'Content-Type': undefined
            },
            data:$scope.formModel,
            transformRequest: angular.identity
        })
        .then(function (response) {
            if(response.data[0]!='П')$scope.error_msg=response.data;
                else $scope.error_msg=response.data.split('\n')[0];
            console.log("Submitted successefuly! response: " + response.data);
            $scope.xdata=response.data.split('\n')[1].split(',');
            $scope.ydata=response.data.split('\n')[2].split(',');
            console.log($scope.xdata);
            console.log($scope.ydata);

            $scope.datapoints=[];
            $scope.items = [];

            for(i=0;i<$scope.xdata.length;i++){
                $scope.datapoints.push({"x":$scope.xdata[i],"y":parseFloat($scope.ydata[i])});
            }

            $scope.datacolumns=[{"id":"y","type":"spline", "color":"red"}];
            $scope.datax={"id":"x"};

            $http({
                method: 'GET',
                url: '/excelreader/getlist'
            }).then(function (response) {
                console.log(response.data);
                var entries=response.data.split('\n');
                for(i=0;i<response.data.split('\n').length-1;i++){
                    var split=entries[i].split('/*/');
                    $scope.items.push({name:split[2]+" ("+split[1]+")",id:split[0]});
                }
            })
        });

    };
});


