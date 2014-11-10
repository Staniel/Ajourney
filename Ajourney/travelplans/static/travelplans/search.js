$(document).ready(function() {

    $('#searchbutton').click(function(e) {
        e.preventDefault();
        // console.log(1);
        var dest = $('#destinationfilter').val().toLowerCase();
        var depart = $('#departfilter').val();
        var ret = $('#returnfilter').val();
        $('#plantable .plan_tr').each(function() {
            $(this).show();
            if (dest != '') {
                var test_dest = $(this).find('.plan_dest').html().toLowerCase();
                if (test_dest.indexOf(dest) <= -1) {
                    $(this).hide();
                }
                return true;
            }
            if (depart != '') {
                var filter_date = new Date(depart);
                var test_depart = $(this).find('.plan_dep').html();
                var arr = test_depart.split("-");
                var this_date = new Date(arr[2], arr[0] - 1, arr[1]);

                if (this_date < filter_date) {
                    $(this).hide();
                    return true;
                }
            }
            if (ret != '') {
                var filter_date = new Date(ret);
                var test_return = $(this).find('.plan_ret').html();
                var arr = test_return.split("-");
                var this_date = new Date(arr[2], arr[0] - 1, arr[1]);
                if (this_date > filter_date) {
                    $(this).hide();
                    return true;
                }
            }
        })
    });
});