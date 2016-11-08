var app = angular.module('gvai', [
     'ui.router',
     'restangular'
 ])

 app.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
     // For any unmatched url, send to /route1
 $urlRouterProvider.otherwise("/");
 $stateProvider
 		   .state('songList', {
                    url: "/",
                    templateUrl: "/static/songList.html",
                    controller: "vaicontrol"
                     })
                                                                           
                     })

 app.controller("vaicontrol", ['$scope', 'Restangular', 'CbgenRestangular', '$q',
 function ($scope, Restangular, CbgenRestangular, $q) {
 $scope.songs = [] 
 $http.get('/songs').success(function(data){ 
	$scope.songs = data; 
}); 
 
 
 }])
