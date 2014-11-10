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
     $('#editform').validate({
    rules: {
        editdestination: {
            required: true
        },
        editdeparttime: {
            required: true,
        },
        editreturntime: {
            required: true,
            greaterThan: "#editdepart"
        },
        editlimit:{
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
    
});