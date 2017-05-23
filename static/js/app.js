var myFirebaseRef;
var chart;
var chartData=[];

$(document).ready(function() {
    d3.json("http://arasunu.softnando.com.net/api/v1/json/", function(data) {
        console.log(data);
        myFirebaseRef = data;
    });
    // requestData();
})

requestData = function(){
    myFirebaseRef.on("values", function(data) {
        var temp = data.val();
        console.log(temp);
    })
}