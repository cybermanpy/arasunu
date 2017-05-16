var myFirebaseRef;
var chart;
var chartData=[];

$(document).ready(function() {
    myFirebaseRef = new Firebase("http://arasunu.softnando.com.net/api/v1/json/");

    requestData();
})

requestData = function(){
    myFirebaseRef.on("value", function(data) {
        var comidas = data.val();
        console.log(comidas);
    })
}


// var myDb;
// var chart;
// var chartData=[];

// $(document).ready(function(){
//     myDb = new Firebase("http://arasunu.softnando.com.net/api/v1/json/");
//     requestData();
// })

// requestData = function(){
//     myDb.on("value", function(data){
//         var temp = data.val();
//         console.log(temp);
//     })
// }