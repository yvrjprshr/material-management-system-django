$(document).ready(function(){
    $('#categoryid').change(function(){
      $.getJSON("/getsubcategoryjson",{ajax:true,cid:$('#categoryid').val()},function(data){
      $('#subcategoryid').empty()
        $('#subcategoryid').append($('<option>').text('-SubCategory-'))
     $.each(data,function(index,item){
     $('#subcategoryid').append($('<option>').text(item[2]).val(item[1]))
     })
     })
         })

    $('#producticon').change(function () {
      var file=producticon.files[0]
      pic.src=URL.createObjectURL(file)

  })
  })
