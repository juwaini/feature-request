angular.module('frApp', [])
    .controller('frAppCtrl', function($scope, $http) {

        $scope.frForm = {};
        $scope.clientForm = {};
        $scope.clientTable = $('#client-table').DataTable();
        $scope.featureRequestTable = $('#feature-request-table').DataTable();
        $scope.featureRequestModal = $('#feature-request-modal');
        $scope.clientModal = $('#client-modal');

        $scope.init = function() {
            this.clientTable.ajax.url('/api/datatables/client/').load();
            this.featureRequestTable.ajax.url('/api/datatables/feature-request/').load();
            $http.get('/api/dropdown/client/').then(function(data)  {
                            $scope.clientsData = data;
                            console.log($scope.clientsData);
                            )
            }
        };

        $scope.onFeatureRequestSubmit = function() {
            var url = '/api/feature-request/create'
            var data = JSON.stringify($scope.frForm)
            console.log(data)
            $http.post(url, data)
            .then(
                    function(res) {
                        alert(res.data)
                        $scope.featureRequestTable.ajax.reload()
                        $scope.frForm = {}
                        $scope.featureRequestModal.modal('hide')
                    },
                    function(err) {
                        console.log(err)
                    }  
                ) 
        };

        $scope.onClientSubmit = function() {
            var url = '/api/client/create'
            var data = JSON.stringify($scope.clientForm)
            console.log(data)
            $http.post(url, data)
            .then(
                    function(res) {
                        alert(res.data)
                        $scope.clientTable.ajax.reload()
                        $scope.clientForm = {}
                        $scope.clientModal.modal('hide')
                    },
                    function(err) {
                        console.log(err)
                    }
                )
        };

        $scope.formReset = function() {
            this.frForm = {}    
        };
    })
