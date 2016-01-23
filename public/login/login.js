'use strict';

angular.module('FutureConnect.login', [
    'ngRoute',
])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/login', {
                templateUrl: 'login/login.html',
                controller: 'loginCtrl'
            });
    }])

    .controller('loginCtrl', function($scope, $rootScope, $http, $location) {
        $scope.Test = 'This is the login page';

        $scope.email = '';
        $scope.password = '';
        $scope.message = 'Login';

        $scope.submitForm = function() {
            $http({
                method: 'POST',
                url: $rootScope.backendURL + 'login',
                data: {
                    'email': $scope.email,
                    'password': $scope.password
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            }).success(function(data, status, headers, config) {
                console.log(data);
                if(data['Response'] == 'True'){
                    $location.path('/Landing');
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