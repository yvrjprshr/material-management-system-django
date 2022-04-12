$(document).ready(function() {
    $('#pattern').keyup(function () {
        $.getJSON("/displayfinalproductalljson", {ajax: true, pattern: $('#pattern').val()}, function (data) {
            var htm = "<table class='table'><thead><tr><th> ID </th><th>Product name </th><th>Stock</th><th>Price</th></tr></thead>"


       $.each(data,function(index,item){
        htm+="<tr><th scope='row'>"+item.finalproductid+"</th><td>"+item.finalproductname+"</td><td>"+item.stock+"</td><td>"+item.price+"</td></tr>"
     })
            htm+="</tbody></table>"
     $('#result').html(htm)

     })
      })
      })






