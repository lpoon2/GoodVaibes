var express = require('express');
var app = express();

var jq = require('json-sql')();
var unflatten = require('flat').unflatten
var mysql = require('mysql');
var squel = require('squel');

var con = mysql.createConnection({
        host : "localhost",
        user : "root",
        password: "cs411fa2016",
        database : "goodVaibes"
});
con.connect(function(err){
        if(err){
        console.log('error connecting to mysql');
        return;
}
        console.log('mysql connection success');
})
var connection_end= function(){
 con.end();
}
app.use(express.static(__dirname + '/public'));

var port = process.env.PORT || 3000;
console.log("Express server running on " + port);
app.listen(process.env.PORT || port);
