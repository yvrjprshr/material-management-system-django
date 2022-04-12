$(document).ready(function(){
     $.getJSON("/getcategoryjson",{ajax:true},function(data){

     $.each(data,function(index,item){
     $('#categoryid').append($('<option>').text(item[1]).val(item[0]))
     })
     })
      })
  //
  //   $('#categoryid').change(function(){
  //         alert("Hii")
  //     $.getJSON("/getsubcategoryjson",{ajax:true,cid:$('#categoryid')},function(data){
  //         alert("Hii")
  //         alert(data)
  //     $('#subcategoryid').empty()
  //       $('#subcategoryid').append($('<option>').text('-SubCategory-'))
  //    $.each(data,function(index,item){
  //    $('#subcategoryid').append($('<option>').text(item[2]).val(item[1]))
  //    })
  //    })
  //        })
  // //       $('#producticon').change(function () {
  // //     var file=producticon.files[0]
  // //     pic.src=URL.createObjectURL(file)
  // //
  // // })

