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

    .filter('unique', function() {
        return function (arr, field) {
            var o = {}, i, l = arr.length, r = [];
            for(i=0; i<l;i+=1) {
                o[arr[i][field]] = arr[i];
            }
            for(i in o) {
                r.push(o[i]);
            }
            return r;
        };
    })