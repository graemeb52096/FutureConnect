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

        $scope.submitForm = function() {
            if ($scope.role == 1){
                var registration_data = {
                    'email': $scope.email,
                    'first': $scope.fName,
                    'last': $scope.lName,
                    'bio': $scope.bio,
                    'role': $scope.role,
                    'school': $scope.school,
                    'password': $scope.password
                }
            }
            else{
                var registration_data = {
                    'email': $scope.email,
                    'first': $scope.fName,
                    'last': $scope.lName,
                    'bio': $scope.bio,
                    'school': $scope.school,
                    'role': $scope.role,
                    'major': $scope.major,
                    'password': $scope.password
                }
            }

            $http({
                method: 'POST',
                url: $rootScope.backendURL + 'register',
                data: registration_data,
                headers: {
                    'Content-Type': 'application/json'
                }
            }).success(function(data, status, headers, config) {
                console.log(data);
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