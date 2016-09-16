angular.module('frApp', [])
    .controller('frAppCtrl', function($scope, $http) {

        $scope.frForm = {};
        $scope.clientForm = {};
        $scope.clientTable = $('#client-table').DataTable();
        $scope.featureRequestTable = $('#feature-request-table').DataTable();

        $scope.init = function() {
            this.clientTable.ajax.url('/api/datatables/client/').load()
            this.featureRequestTable.ajax.url('/api/datatables/feature-request/').load()
        };

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
