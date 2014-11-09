
$(document).ready(function(){
    $.validator.addMethod("greaterThan", 
    function(value, element, params) {
        if (!/Invalid|NaN/.test(new Date(value))) {
            return new Date(value) > new Date($(params).val());
        }
        return isNaN(value) && isNaN($(params).val()) 
            || (Number(value) > Number($(params).val())); 
    },'return time must be greater than depart time.');
    $('#createform').validate({
    rules: {
        destination: {
            required: true
        },
        departtime: {
            required: true,
        },
        returntime: {
            required: true,
            greaterThan: "#newdepart"
        },
        limit:{
            required: true,
            min: 2,
            digits: true
        }
    },
    highlight: function (element) {
        $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },
    errorClass: 'help-block',
    success: function (element) {
        element.text('OK!').addClass('valid')
            .closest('.form-group').removeClass('has-error').addClass('has-success');
    }
});
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
        $('#plantable .plan_tr').each(function(){
            $(this).show();
            if (dest != '')
            {
                var test_dest = $(this).find('.plan_dest').html().toLowerCase();
                if (test_dest.indexOf(dest) <= -1)
                {
                    $(this).hide();
                }
<<<<<<< HEAD
                    return true;
=======
                    return true;   
>>>>>>> ec8d6766af557d0e48a7446c0878f44d453b13ba
            }
            if (depart != '')
            {
                var filter_date = new Date(depart);
                var test_depart = $(this).find('.plan_dep').html();
                var arr = test_depart.split("-");
                var this_date = new Date(arr[2], arr[0]-1, arr[1]);

                if (this_date < filter_date)
                {
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
