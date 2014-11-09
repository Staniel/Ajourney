$(document).ready(function(){

    $('#allplan').click(function(e){
        e.preventDefault();
       $.get('/travelplans/available_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#myplan').click(function(e){
        e.preventDefault();
       $.get('/travelplans/my_plans', function(data){
         $("#updatecontent").html(data);
        });
    });
    $('#jplan').click(function(e){
        e.preventDefault();
       $.get('/travelplans/joined_plans', function(data){
         $("#updatecontent").html(data);
        });
    });

      $('#searchbutton').click(function(e){
        e.preventDefault();
        // console.log(1);
        var dest = $('#destinationfilter').val().toLowerCase();
        var depart = $('#departfilter').val();
        var ret = $('#returnfilter').val();
        // console.log(depart);
        // console.log(ret);
        $('#plantable .plan_tr').each(function(){
            $(this).show();
            if (dest != '')
            {
                var test_dest = $(this).find('.plan_dest').html().toLowerCase();
                if (test_dest.indexOf(dest) <= -1)
                {
                    $(this).hide();
                    return true;
                }    
            }
            if (depart != '')
            {
                var filter_date = new Date(depart);
                var test_depart = $(this).find('.plan_dep').html();
                var arr = test_depart.split("-");
                var this_date = new Date(arr[2], arr[0]-1, arr[1]);

                if (this_date < filter_date)
                {
                    console.log(this_date);
                    console.log(filter_date);
                    $(this).hide();
                    return true;
                }
            }
            if (ret != '')
            {
                var filter_date = new Date(ret);
                var test_return = $(this).find('.plan_ret').html();
                var arr = test_return.split("-");
                var this_date = new Date(arr[2], arr[0]-1, arr[1]);
                if (this_date > filter_date)
                {
                    $(this).hide();
                    return true;
                }
            }
        })
        
    }); 

    }); 
