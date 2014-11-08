$(document).ready(function(){
    $('#allplan').click(function(){
       $.get('/travelplans/view_available_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#myplan').click(function(){
       $.get('/travelplans/view_my_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#jplan').click(function(){
       $.get('/travelplans/view_joined_plans', function(data){
         $("#updatecontent").html(data);
        });

    });    
});