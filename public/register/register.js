'use strict';

'use strict';

angular.module('FutureConnect.register', [
    'ngRoute',
])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/register', {
                templateUrl: 'register/register.html',
                controller: 'registerCtrl'
            });
    }])

    .controller('registerCtrl', function($scope, $rootScope, $http, $location) {

        $scope.email = '';
        $scope.fName = '';
        $scope.lName = '';
        $scope.password = '';
        $scope.password1 = '';
        $scope.bio = '';
        $scope.role = '';
        $scope.school = '';
        $scope.major = '';

        if ($scope.role == 1){
            var data = {

            }
        }



        $scope.submitForm = function() {
            $http({
                method: 'POST',
                url: $rootScope.backendURL + 'register',
                data: {

                },
                headers: {
                    'Content-Type': 'application/json'
                }
            }).success(function(data, status, headers, config) {
                console.log(data);
                if(data['Response'] == 'True'){
                    $rootScope.logged = true;
                    $rootScope.user = data['Data']
                    $location.path('/landing');
                }
                else{
                    $scope.message = data['Message'];
                }
            }).error(function(data, status, headers, config) {
                console.log('error');
                console.log(arguments);
            });
        }

    })

    .run(function($rootScope) {
        var login_Post = {
            method: 'POST',
            url: $rootScope.backendURL + 'login'
        }
    })