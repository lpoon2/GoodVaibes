var gvControllers = angular.module('gvControllers', ['ngMaterial']);

gvControllers.controller('songController', ['$scope', 'CommonData','Vai' , function($scope, CommonData,Vai) {
  $scope.things = {}
    $scope.data = CommonData.getData();
    Vai.get_all()
    .success(function(data){
      $scope.things = data.data;
    });
    
    $scope.song = {
         title: '',
         genre: '',
         language: 'English',
         record_label: '',
       };
    $scope.song.saved = false; 
    $scope.add = function(){
      Vai.post_song($scope.song)
      .success(function(data){
            $scope.song = {};
        })
      .then(function(){

      });
    }

}]).config(function($mdThemingProvider) {

    // Configure a dark theme with primary foreground yellow
    //
         $mdThemingProvider.theme('docs-dark', 'default')
               .primaryPalette('yellow')
                     .dark();
    
                       });
    

