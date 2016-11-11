var app = angular.module('goodvai', ['ngRoute', 'gvControllers', 'gvServices']);

app.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
    when('/songs', {
    templateUrl: '/static/songList.html',
    controller: 'songController'
  }).
  when('/', {
    templateUrl: '/static/partials/songList.html',

    controller: 'songController'
  }).
  otherwise({
    redirectTo: '/'
  });
}]);

var gvServices=angular.module("gvServices",[]);
gvServices.factory("CommonData",function(){
  var data="";
  return{
    getData:function(){return data},

    setData:function(newData){data=newData}}}),

//var gvServices=angular.module("gvServices",[]);
gvServices.factory("Vai",function($http,$window){
  var baseUrl="http://fa16-cs411-25.cs.illinois.edu:8000"
  return{
    get_all:function(){
      return $http.get(baseUrl+"/api/songs");
    },
    post_song: function(data){

      return $http.post(baseUrl+"/api/songs", data);
    },
    get_one:function(id){
      return $http.get(baseUrl+"/api/users/"+id);
    },
    mod_user:function(id, data){
      return $http.put(baseUrl+"/api/users/"+id, data);
    },
    delete_user : function(id){
      return $http.delete(baseUrl+"/api/users/"+id);
    },
    get_all_task: function(){
      return $http.get(baseUrl+"/api/tasks");
    },
    creat_task: function(data){
      return $http.post(baseUrl+"/api/tasks", data);
    },
    get_one_task: function(id){
      return $http.get(baseUrl+"/api/tasks/"+id);
    },
    mod_task:function(id, data){
      return $http.put(baseUrl+"/api/tasks/"+id, data);
    },
    delete_task : function(id){
      return $http.delete(baseUrl+"/api/tasks/"+id);
    },
  }
}
  );
