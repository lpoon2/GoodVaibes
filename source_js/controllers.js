var squel = require('squel');
app.controller('listController', ['$scope', '$http','$filter','myService', function($scope, $http,$filter,myService) {
  $scope.infos={};
  $scope.details={};
  //////////////////mp3
  $http.get('../data/imdb250.json')
      .success(function(data) {
          $scope.infos = data;
          console.log(data);
      })
      .error(function(data) {
          console.log('Error: ' + data);
      });

  $scope.getinfo = function(name){
    var found = $filter('getByRank')($scope.infos, name);
    window.top.location = "details.html"+ '?rank='+ found.rank;
  //  myService.set(found);
  }
  /////////////////mp3
  var insert = function(sql){
con.query(sql, function(err, rows){
                if(err) throw err;
});
}
   $scope.song_insert = function(name){
    wtf_wikipedia.from_api(name, function(page) {
    var parsed = wtf_wikipedia.parse(page); // causes the crash

          var shit = squel.insert().into('Song').set('title',parsed.infobox.Name.text)
                                   .set('genre',parsed.infobox.Genre.text).set('record_label', parsed.infobox.Label.text)
                                         .toString();
                      insert(shit);

                  });
  }

}]);

app.controller('detailsController', ['$scope', '$http','$filter','myService', function($scope, $http,$filter,myService) {
  $scope.details = {};
  $scope.movies={};


  $scope.getRank = function(a){
    $http.get('../data/imdb250.json')
        .success(function(data) {
            $scope.movies = data;
            var found = $filter('getByRank')($scope.movies, parseInt(a));
            $scope.details = found;
            console.log(found);
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });

    };
    $scope.left = function(){
      var found = $filter('getByRank')($scope.movies, $scope.details.rank - 1);
      if(found == null) found = $filter('getByRank')($scope.movies, 250);
      $scope.details = found;
      console.log(found);
    };
    $scope.right = function(){
      var found = $filter('getByRank')($scope.movies, $scope.details.rank + 1);
      if(found == null) found = $filter('getByRank')($scope.movies, 1);
      $scope.details = found;

      console.log(found);
    };
}]);
// app.factory('myService', function() {
//  var savedData = {}
//  function set(data) {
//    savedData = data;
//  }
//  function get() {
//    alert(savedData.title);
//   return savedData;
//  }
//  return {
//   set: set,
//   get: get
//  }
// });
app.service('myService', function Service(){
  var details = {};
  this.set = function(obj){
    console.log(obj);
    this.details = obj;
  };
  this.get = function(){
    console.log(details);
    return details;
  };
});
app.filter('getByRank', function() {
  return function(input, id) {
    var i=0, len=input.length;
    for (; i<len; i++) {
      if (+input[i].rank == +id) {
        return input[i];
      }
    }
    return null;
  }
});
