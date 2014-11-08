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
            if (dest != '')
            {
                var test_dest = $(this).find('.plan_dest').html().toLowerCase();
                if (test_dest != dest)
                {
                    $(this.remove());
                }
            }
        })
        $('#plantable .plan_tr').each(function(){
            if (depart != '')
            {
                var test_depart = $(this).find('.plan_dep').html();
                var filter_date = new Date(depart);
                var this_date = new Date(test_depart);
                console.log(filter_date);
                console.log(test_depart);
                // remove if the plan depart before the filter time
                if (this_date < filter_date)
                {
                    console.log(test_depart);
                    $(this.remove());
                }
            }
        })
        $('#plantable .plan_tr').each(function(){
            if (ret != '')
            {
                var test_ret = $(this).find('.plan_ret').html();
                // remove if the plan return after the filter time
                if (new Date(test_ret) > new Date(ret))
                {
                    $(this.remove());
                }
            }
        })
        
    }); 

    }); 
