//form Submit
$("form").submit(function(evt){	 
    evt.preventDefault();
    var formData = new FormData($(this)[0]);
$.ajax({
    url: '/api/v1/upload/',
    type: 'POST',
    data: formData,
    async: false,
    cache: false,
    contentType: false,
    enctype: 'multipart/form-data',
    processData: false,
    success: function (response) {
        var retrun_data = jQuery.parseJSON(response);
        $("#edtDecodeText").attr('value', retrun_data['text']);
    }
});
return false;
});
