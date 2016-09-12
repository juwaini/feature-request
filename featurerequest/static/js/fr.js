angular.module('frApp', [])
    .controller('frAppCtrl', function($scope, $http) {

        $scope.frForm = {};

        $scope.onSubmit = function() {
            console.log("Triggering formSubmit()!")
        };
    })
