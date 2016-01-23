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

    .controller('loginCtrl', ['$rootScope, $scope', function($rootScope, $scope) {
        $scope.Test = 'This is the login page';

        var login_Post = {
            method: 'POST',
            url: $rootScope.backendURL + 'authenticate'
        }

        $http.post(login_URL, ).success(function(data, status, headers, config) {
            console.log(data);
            $rootScope.Users = data.Users
        }).error(function(data, status, headers, config) {
            console.log('error');
            console.log(arguments);
        });
    }])