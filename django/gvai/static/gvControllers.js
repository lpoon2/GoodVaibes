var gvControllers = angular.module('gvControllers', ['ngMaterial']);

gvControllers.controller('songController', ['$scope','$window','CommonData','Vai' , function($scope,$window, CommonData,Vai) {
  $scope.things = {}
    $scope.data = CommonData.getData();
	console.log("please show"); 	    
    Vai.get_all()
    .success(function(data){
    	  console.log(data[0].fields.title); 
	  $scope.things = data;
    });
    
    $scope.song = {
         title: '',
         genre: '',
         language: 'English',
         record_label: '',
       };
    $scope.realobj = {}
    $scope.add = function(){
	$scope.realobj.fields = $scope.song; 
	$scope.realobj.model = "gvai.song";

      Vai.post_song($scope.realobj)
      .success(function(data){
		
            $scope.realpbj = {};
	   $window.location.reload();       
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
    

