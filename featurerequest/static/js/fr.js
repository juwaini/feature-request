angular.module('frApp', [])
    .controller('frAppCtrl', function($scope, $http) {

        $scope.frForm = {};
        $scope.clientForm = {};

        $scope.onFeatureRequestSubmit = function() {
            var url = '/api/feature-request/create'
            console.log(this.frForm)
            $http.post(url, this.frform).then(function(res){
                alert(res.data)
            })   
        };

        $scope.onClientSubmit = function() {
            var url = '/api/client/create'
            console.log(this.clientForm)
            $http.post(url, this.clientform).then(function(res){
                alert(res.data)
            })   
        };

        $scope.formReset = function() {
            this.frForm = {}    
        };
    })
