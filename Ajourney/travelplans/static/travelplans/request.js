URLBase = "http://localhost:8000/travelplans/";
$(document).ready(function() {
    $.validator.addMethod(
"regex",
function(value, element) {
    return this.optional(element) || !(/:|\?|\$|\%|\&|\/|\\|\*|\"|<|>|\||%/g.test(value));
},
    "Illegal character are not allowed.");

    $.validator.addMethod("greaterThan",
        function(value, element, params) {
            if (!/Invalid|NaN/.test(new Date(value))) {
                return new Date(value) >= new Date($(params).val());
            }
            return isNaN(value) && isNaN($(params).val()) || (Number(value) > Number($(params).val()));
        }, 'return time must be greater than depart time.');
    $('#createform').validate({
        rules: {
            destination: {
                required: true,
                regex: true
            },
            departtime: {
                required: true,
            },
            returntime: {
                required: true,
                greaterThan: "#newdepart"
            },
            limit: {
                required: true,
                min: 2,
                digits: true
            }
        },
        submitHandler: function(e) {
            var postData = $("#createform").serializeArray();
            var formURL = $("#createform").attr("name");
            $.ajax({
                url: formURL,
                type: "POST",
                data: postData,
                success: function(data) {
                    if (data.indexOf("error") > -1)
                        alert(data);
                    else
                        location.href = URLBase + "my_plans";
                },
                error: function(jqXHR, textStatus, errorThrown) {}
            });
        },
        highlight: function(element) {
            $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        errorClass: 'help-block',
        success: function(element) {
            element.text('OK!').addClass('valid')
                .closest('.form-group').removeClass('has-error').addClass('has-success');
        }
    });
    $('#editform').validate({
        rules: {
            editdestination: {
                required: true,
                regex: true
            },
            editdepart: {
                required: true,
            },
            editreturn: {
                required: true,
                greaterThan: "#editdepartid"
            },
            editlimit: {
                required: true,
                min: 2,
                digits: true
            }
        },
        submitHandler: function(e) {
            var postData = $("#editform").serializeArray();
            var formURL = $("#editform").attr("name");
            $.ajax({
                url: formURL,
                type: "POST",
                data: postData,
                success: function(data) {
                    if (data.indexOf("error") > -1)
                        alert(data);
                    location.reload();
                },
                error: function(jqXHR, textStatus, errorThrown) {}
            });
        },
        highlight: function(element) {
            $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        errorClass: 'help-block',
        success: function(element) {
            element.text('OK!').addClass('valid')
                .closest('.form-group').removeClass('has-error').addClass('has-success');
        }
    });

    $('#deleteform').submit(function(e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        var postData = $("#deleteform").serializeArray();
        var formURL = $("#deleteform").attr("name");
        $.ajax({
            url: formURL,
            type: "POST",
            data: postData,
            success: function(data) {
                if (data.indexOf("error") > -1)
                    alert(data);
                else {
                    location.href = URLBase + "my_plans";
                    // alert("successful delete");
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {}
        });
    });
    $('#shareform').submit(function(e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        var postData = $("#shareform").serializeArray();
        var formURL = $("#shareform").attr("name");
        $.ajax({
            url: formURL,
            type: "POST",
            data: postData,
            success: function(data) {
                if (data.indexOf("error") > -1)
                    alert(data);
                else {
                    // alert("success");
                    location.reload();
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {}
        });
    });
    $('#joinform').submit(function(e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        var postData = $("#joinform").serializeArray();
        var formURL = $("#joinform").attr("name");
        $.ajax({
            url: formURL,
            type: "POST",
            data: postData,
            success: function(data) {
                if (data.indexOf("error") > -1)
                    alert(data);
                else {
                    // alert("success");
                    location.reload();
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {}
        });
    });
    $('#unjoinform').submit(function(e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        var postData = $("#unjoinform").serializeArray();
        var formURL = $("#unjoinform").attr("name");
        $.ajax({
            url: formURL,
            type: "POST",
            data: postData,
            success: function(data) {
                if (data.indexOf("error") > -1)
                    alert(data);
                else {
                    // alert("success");
                    location.reload();
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {}
        });
    });
});
