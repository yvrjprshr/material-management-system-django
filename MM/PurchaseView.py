from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
import uuid
import os
import random

def PurchaseInterface(request):
   try:
       result = request.session['EMPLOYEE']
       return render(request,"PurchaseInterface.html",{'result':result})
   except Exception as e:
       print("error:",e)
       return render(request, "EmployeeLogin.html", {'result': result})


def PurchaseProductSubmit(request):
    try:
       categoryid = request.POST['categoryid']
       subcategoryid = request.POST['subcategoryid']
       productid= request.POST['productid']
       finalproductid = request.POST['finalproductid']
       datepurchase = request.POST['datepurchase']
       supplierid=request.POST['supplierid']
       stock = request.POST['stock']
       amount = request.POST['price']

       db, cmd = Pool.ConnectionPool()
       q="insert into Purchase(categoryid, subcategoryid, productid, finalproductid, datepurchase, supplierid, stock, amount)values({},{},{},{},'{}',{},{},{} )".format(categoryid, subcategoryid, productid, finalproductid, datepurchase, supplierid, stock, amount)
       cmd.execute(q)
       #update stock
       q="update finalproducts set price=((price + {})/2),stock=stock+{} where finalproductid={}".format(amount,stock,finalproductid)
       cmd.execute(q)
       db.commit()
       db.close()
       return render(request, "PurchaseInterface.html", {'msg': 'Record Submitted Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request, "PurchaseInterface.html",{'msg':'Record Submission Failed'})

#
# def DisplayAllPurchase(request):
#     try:
#         db,cmd=Pool.ConnectionPool()
#         q="select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid),(select SC.subcategoryname from subcategories SC where SC.subcategoryid=P.subcategoryid) from Purchases P"
#         cmd.execute(q)
#         rows=cmd.fetchall()
#
#         db.close()
#         return render(request,"DisplayAllPurchase.html",{'rows':rows})
#     except Exception as e:
#         return render(request, "DisplayAllPurchase.html", {'rows': []})
#
# def DisplayPurchaseById(request):
#     try:
#         pid=request.GET['pid']
#         db,cmd=Pool.ConnectionPool()
#         q = "select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid),(select sc.subcategoryname from subcategories sc where sc.subcategoryid=p.subcategoryid) from Purchases p where Purchaseid={}".format(pid)
#         cmd.execute(q)
#         row=cmd.fetchone()
#
#         db.close()
#         return render(request,"DisplayPurchaseById.html",{'row':row})
#     except Exception as e:
#         print("error:",e)
#         return render(request, "DisplayPurchaseById.html", {'row': []})
#
# def EditDeletePurchaseRecord(request):
#     btn=request.GET['btn']
#     pid = request.GET['pid']
#     if(btn=="Edit"):
#       # cid = request.GET['cid']
#       # scid = request.GET['scid']
#       cid = request.GET['categoryid']
#       scid = request.GET['subcategoryid']
#
#       Purchasename = request.GET['Purchasename']
#       pdescription = request.GET['pdescription']
#       try:
#         db,cmd=Pool.ConnectionPool()
#         q = "update Purchases set categoryid={},subcategoryid={},Purchasename='{}',pdescription='{}' where Purchaseid={} ".format(cid,scid,Purchasename,pdescription,pid)
#         cmd.execute(q)
#         db.commit()
#
#         db.close()
#         return DisplayAllPurchase(request)
#       except Exception as e:
#         print("error:",e)
#         return DisplayAllPurchase(request)
#     elif(btn=="Delete"):
#         try:
#             db, cmd = Pool.ConnectionPool()
#             q = "Delete from Purchases where Purchaseid={}".format(pid)
#             cmd.execute(q)
#             db.commit()
#             db.close()
#             return DisplayAllPurchase(request)
#         except Exception as e:
#             print("error:", e)
#             return DisplayAllPurchase(request)
#
# def EditPurchaseIcon(request):
#     try:
#         pid=request.GET['pid']
#         Purchasename=request.GET['Purchasename']
#         Purchaseicon=request.GET['Purchaseicon']
#         row=[pid,Purchasename,Purchaseicon]
#         return render(request,"EditPurchaseIcon.html",{'row':row})
#     except Exception as e:
#         print("error:",e)
#         return render(request,"EditPurchaseIcon.html",{'row':[]})
#
# def SaveEditIcon(request):
#     try:
#        pid=request.POST['pid']
#        oldpicture = request.POST['oldpicture']
#        Purchaseicon=request.FILES['Purchaseicon']
#        filename=str(uuid.uuid4())+Purchaseicon.name[Purchaseicon.name.rfind('.'):]
#        password="".join(random.sample(['1','a','4','x','6','66','#','@'],k=7))
#        db, cmd = Pool.ConnectionPool()
#        q="update Purchases set Purchaseicon='{}' where Purchaseid={}".format(filename,pid)
#
#        cmd.execute(q)
#        db.commit()
#        F=open("D:/MM/assets/"+filename,"wb")
#        for chunk in Purchaseicon.chunks():
#            F.write(chunk)
#        F.close()
#
#        db.close()
#        os.remove("D:/MM/assets/"+oldpicture)
#        return DisplayAllPurchase(request)
#     except Exception as e:
#        print("error:", e)
#        return DisplayAllPurchase(request)
#
# def GetPurchaseJson(request):
#  try:
#   db,cmd=Pool.ConnectionPool()
#   scid=request.GET['scid']
#   q="select * from Purchases where subcategoryid={}".format(scid)
#   cmd.execute(q)
#   rows=cmd.fetchall()
#   db.close()
#   return JsonResponse(rows,safe=False)
#
#  except Exception as e:
#   print(e)
#   return JsonResponse([],safe=False)
#
