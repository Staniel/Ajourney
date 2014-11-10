URLBase = "http://localhost:8080/travelplans/";
$(document).ready(function(){     

        $('#editbutton').click(function(e){
       var postData = $("#editform").serializeArray();
       var formURL = $("#editform").attr("name");
       $.ajax({
        url: formURL,
        type: "POST",
        data: postData,
        success:function(data){
            if (data.indexOf("error") > -1)
                alert(data);
            location.reload();
        },
        error: function(jqXHR, textStatus, errorThrown){
        }
       });
    });

    $('#createbutton').click(function(e){
       var postData = $("#createform").serializeArray();
       var formURL = $("#createform").attr("name");
       $.ajax({
        url: formURL,
        type: "POST",
        data: postData,
        success:function(data){
            if (data.indexOf("error") > -1)
                alert(data);
            else
                location.href = URLBase+"my_plans";
        },
        error: function(jqXHR, textStatus, errorThrown){
        }
       });
    });
        $('#deletebutton').click(function(e){
        var postData = $("#createform").serializeArray();
       var formURL = $("#deleteform").attr("name");
       $.ajax({
        url: formURL,
        type: "POST",
        data: postData,
        success:function(data){
            if (data.indexOf("error") > -1)
                alert(data);
            else 
                {location.href = URLBase+"my_plans";alert("successful delete");}
        },
        error: function(jqXHR, textStatus, errorThrown){
        }
       });
    });
        $('#sharebutton').click(function(e){
        var postData = $("#shareform").serializeArray();
       var formURL = $("#shareform").attr("name");
       $.ajax({
        url: formURL,
        type: "POST",
        data: postData,
        success:function(data){
            if (data.indexOf("error") > -1)
                alert(data);
            else 
                {alert("success");location.reload();}
        },
        error: function(jqXHR, textStatus, errorThrown){
        }
       });
    });
});