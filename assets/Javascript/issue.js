$(document).ready(function(){
    var d=new Date()
    var cd=(d.getFullYear())+'-'+(d.getMonth()+1)+'-'+(d.getDate())
    $('#dateissue').val(cd)

    $('#productid').change(function() {
        $.getJSON("/getfinalproductjson", {ajax: true, pid:$('#productid').val()}, function (data) {
            alert(data)
            $('#finalproductid').empty()
            $('#finalproductid').append($('<option>').text('-Final Product-'))
            $.each(data, function (index, item) {
                $('#finalproductid').append($('<option>').text(item[4]).val(item[3]))
            })
             })
         })
  $('#finalproductid').change(function () {
      alert("xx")
        $.getJSON("/displayfinalproductbyidjson", { ajax: true, fid:$('#finalproductid').val() }, function (data) {
            alert(data)
            $('#currentstocks').html(data.stock)
        })
    })

     $('#qtyissue').keyup(function () {
         if(parseInt($('#currentstocks').html())>=parseInt($('#qtyissue').val()))
         {
             $('#btnsubmit').attr('disabled',false)
         }
         else{
             $('#btnsubmit').attr('disabled',true)
         }
     })

             })