$(document).ready(function(){
    $('#allplan').click(function(){
       $.get('/travelplans/available_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#myplan').click(function(){
       $.get('/travelplans/my_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#jplan').click(function(){
       $.get('/travelplans/joined_plans', function(data){
         $("#updatecontent").html(data);
        });

    });    
});