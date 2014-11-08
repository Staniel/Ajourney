$(document).ready(function(){
    type = 1;
    $('#allplan').click(function(){
        type = 1;
       $.get('/travelplans/available_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#myplan').click(function(){
        type = 2;
       $.get('/travelplans/my_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#jplan').click(function(){
        type = 3;
       $.get('/travelplans/joined_plans', function(data){
         $("#updatecontent").html(data);
        });

    });
    //   $('#searchbutton').click(function(){
    //     myurl = 'travelplans/';
    //     if (type == 2)
    //         myurl+='my_plans';
    //     else if (type == 3)
    //         myurl+='joined_plans';
    //     else
    //         myurl+='available_plans';
    //     $.ajax({
    //         type: "POST",
    //         url : myurl,
    //         data: $('form.search').serialize(),
    //         success: function(data){
    //             $('#updatecontent').html(data);
    //         },
    //         error: function(){
    //             console.log("error during searching");
    //         }

    //     });
    // }); 

    }); 
});