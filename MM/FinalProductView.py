from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
from . import  PoolDict
import uuid
import os
import random

def FinalProductInterface(request):
    return render(request,"FinalProductInterface.html")

def FinalProductSubmit(request):
    try:
       categoryid = request.GET['categoryid']
       subcategoryid = request.GET['subcategoryid']
       productid=request.GET['productid']
       finalproductname = request.GET['finalproductname']
       size = request.GET['size']
       sizeunit = request.GET['sizeunit']
       color= request.GET['color']
       weight= request.GET['weight']
       weightunit= request.GET['weightunit']
       price = request.GET['price']
       stock= request.GET['stock']

       db, cmd = Pool.ConnectionPool()
       q="insert into finalproducts(categoryid, subcategoryid, productid,finalproductname,size,sizeunit,color, weight, weightunit, price, stock)values({},{},{},'{}',{},'{}','{}',{},'{}',{},{})".format(categoryid, subcategoryid, productid,finalproductname,size,sizeunit,color, weight, weightunit, price, stock)
       cmd.execute(q)
       db.commit()

       db.close()
       return render(request, "FinalProductInterface.html",{'msg':'Record Successfully Submitted'})

    except Exception as e:
        print("Error:",e)
        return render(request, "FinalProductInterface.html",{'msg':'Record Submission Failed'})


def DisplayAllFinalProduct(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select FP.*,(select C.categoryname from categories C where C.categoryid=FP.categoryid),(select SC.subcategoryname from subcategories SC where SC.subcategoryid=FP.subcategoryid),(select P.productname from products P where P.productid=FP.finalproductid) from finalproducts FP"
        cmd.execute(q)
        rows=cmd.fetchall()

        db.close()
        return render(request,"DisplayAllFinalProduct.html",{'rows':rows})
    except Exception as e:
        print('error:',e)
        return render(request, "DisplayAllFinalProduct.html", {'rows': []})

def DisplayFinalProductByIdJson(request):
    try:
        fid=request.GET['fid']
        db,cmd=PoolDict.ConnectionPool()
        q = "select fp.*,(select c.categoryname from categories c where c.categoryid=fp.categoryid),(select sc.subcategoryname from subcategories sc where sc.subcategoryid=fp.subcategoryid),(select p.productname from products p where p.productid=fp.productid) from finalproducts fp where finalproductid={}".format(fid)
        cmd.execute(q)
        row=cmd.fetchone()

        db.close()
        return JsonResponse(row, safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([], safe=False)

def GetFinalProductJson(request):
 try:
  db,cmd=Pool.ConnectionPool()
  pid=request.GET['pid']
  q="select * from finalproducts where productid={}".format(pid)
  cmd.execute(q)
  rows=cmd.fetchall()
  db.close()
  return JsonResponse(rows,safe=False)

 except Exception as e:
  print(e)
  return JsonResponse([],safe=False)

def DisplayFinalProductAllJson(request):
    try:
        pattern=request.GET['pattern']
        db,cmd=PoolDict.ConnectionPool()
        q = "select fp.*,(select c.categoryname from categories c where c.categoryid=fp.categoryid),(select sc.subcategoryname from subcategories sc where sc.subcategoryid=fp.subcategoryid),(select p.productname from products p where p.productid=fp.productid) from finalproducts fp where finalproductname like '%{}%'".format(pattern)
        cmd.execute(q)
        rows=cmd.fetchall()

        db.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([], safe=False)

def DisplayUpdatedStock(request):
    return render(request,"ListProductsEmployee.html")



# def DisplayProductById(request):
#     try:
#         pid=request.GET['pid']
#         db,cmd=Pool.ConnectionPool()
#         q = "select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid),(select sc.subcategoryname from subcategories sc where sc.subcategoryid=p.subcategoryid) from products p where productid={}".format(pid)
#         cmd.execute(q)
#         row=cmd.fetchone()
#
#         db.close()
#         return render(request,"DisplayProductById.html",{'row':row})
#     except Exception as e:
#         print("error:",e)
#         return render(request, "DisplayProductById.html", {'row': []})
#
# def EditDeleteProductRecord(request):
#     btn=request.GET['btn']
#     pid = request.GET['pid']
#     if(btn=="Edit"):
#       # cid = request.GET['cid']
#       # scid = request.GET['scid']
#       cid = request.GET['categoryid']
#       scid = request.GET['subcategoryid']
#
#       productname = request.GET['productname']
#       pdescription = request.GET['pdescription']
#       try:
#         db,cmd=Pool.ConnectionPool()
#         q = "update products set categoryid={},subcategoryid={},productname='{}',pdescription='{}' where productid={} ".format(cid,scid,productname,pdescription,pid)
#         cmd.execute(q)
#         db.commit()
#
#         db.close()
#         return DisplayAllProduct(request)
#       except Exception as e:
#         print("error:",e)
#         return DisplayAllProduct(request)
#     elif(btn=="Delete"):
#         try:
#             db, cmd = Pool.ConnectionPool()
#             q = "Delete from products where productid={}".format(pid)
#             cmd.execute(q)
#             db.commit()
#             db.close()
#             return DisplayAllProduct(request)
#         except Exception as e:
#             print("error:", e)
#             return DisplayAllProduct(request)
#
# def EditProductIcon(request):
#     try:
#         pid=request.GET['pid']
#         productname=request.GET['productname']
#         producticon=request.GET['producticon']
#         row=[pid,productname,producticon]
#         return render(request,"EditProductIcon.html",{'row':row})
#     except Exception as e:
#         print("error:",e)
#         return render(request,"EditProductIcon.html",{'row':[]})
#
# def SaveEditIcon(request):
#     try:
#        pid=request.POST['pid']
#        oldpicture = request.POST['oldpicture']
#        producticon=request.FILES['producticon']
#        filename=str(uuid.uuid4())+producticon.name[producticon.name.rfind('.'):]
#        password="".join(random.sample(['1','a','4','x','6','66','#','@'],k=7))
#        db, cmd = Pool.ConnectionPool()
#        q="update products set producticon='{}' where productid={}".format(filename,pid)
#
#        cmd.execute(q)
#        db.commit()
#        F=open("D:/MM/assets/"+filename,"wb")
#        for chunk in producticon.chunks():
#            F.write(chunk)
#        F.close()
#
#        db.close()
#        os.remove("D:/MM/assets/"+oldpicture)
#        return DisplayAllProduct(request)
#     except Exception as e:
#        print("error:", e)
#        return DisplayAllProduct(request)
