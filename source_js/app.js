var app = angular.module('mp3',['ngRoute']);
app.config(function ($routeProvider) {
    $routeProvider
        .when('/list', {
            templateUrl : '../partials/list.html',
            controller: 'listController'
        })
        .when('/details', {
            templateUrl : '../partials/details.html',
        });
});
