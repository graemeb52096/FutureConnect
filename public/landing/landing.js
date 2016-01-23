'use strict';

angular.module('FutureConnect.landing', [
    'ngRoute',
])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/landing', {
                templateUrl: 'landing/landing.html',
                controller: 'landingCtrl'
            });
    }])

    .controller('landingCtrl', function($scope, $rootScope, $location) {
        if ($rootScope.logged){
            $scope.test = 'Landing page'

        }
        else{
            $location.path('/login');
        }
    })

    .run(function($rootScope) {
        var login_Post = {
            method: 'POST',
            url: $rootScope.backendURL + 'login'
        }
    })