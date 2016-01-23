'use strict';

angular.module('FutureConnect', [
    'ngRoute',
    'FutureConnect.login',
    'FutureConnect.landing',
])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                redirectTo: '/login/'
            })
    }])
    .run(function($rootScope, $location, $http) {
        var devbackendURL =  'http://127.0.0.1:5000/';

        var backendURL = devbackendURL;

        $rootScope.backendURL = backendURL;
        var main_URL = backendURL + 'Users';

        $http.get(main_URL).success(function(data, status, headers, config) {
            console.log(data);
            $rootScope.Users = data.Users
        }).error(function(data, status, headers, config) {
            console.log('error');
            console.log(arguments);
        });
    })
    .controller('FutureConnectCtrl', function($rootScope) {

    })