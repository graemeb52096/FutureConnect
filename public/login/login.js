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

    .controller('loginCtrl', ['$scope', function($scope) {
        $scope.Test = 'This is the login page';

    }])

    .run(function($rootScope) {
        var login_Post = {
            method: 'POST',
            url: $rootScope.backendURL + 'authenticate'
        }
    })