$(document).ready(function(){
    $('#subcategoryid').change(function() {
        $.getJSON("/getproductjson", {ajax: true, scid:$('#subcategoryid').val()}, function (data) {
            $('#productid').empty()
            $('#productid').append($('<option>').text('-Product-'))
            $.each(data, function (index, item) {
                $('#productid').append($('<option>').text(item[3]).val(item[2]))
            })
             })
         })
})

