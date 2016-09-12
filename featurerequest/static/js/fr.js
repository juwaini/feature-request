angular.module('frApp', [])
    .controller('frAppCtrl', function($scope, $http) {

        $scope.frForm = {};

        $scope.onSubmit = function() {
            var url = '/api/feature-request/create'
            console.log(this.frForm)
            $http.post(url, this.frform).then(function(res){
                this.formReset()
            })   
        };

        $scope.formReset = function() {
            this.frForm = {}    
        };
    })
