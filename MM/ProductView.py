from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
import uuid
import os
import random

def ProductInterface(request):
    return render(request,"ProductInterface.html")
def ProductSubmit(request):
    try:
       categoryid = request.POST['categoryid']
       subcategoryid = request.POST['subcategoryid']
       productname=request.POST['productname']
       pdescription = request.POST['pdescription']
       producticon =request.FILES['producticon']


       filename=str(uuid.uuid4())+producticon.name[producticon.name.rfind('.'):]
       db, cmd = Pool.ConnectionPool()
       q="insert into products(categoryid,subcategoryid,productname,pdescription,producticon)values({},{},'{}','{}','{}')".format(categoryid,subcategoryid,productname,pdescription,filename)
       cmd.execute(q)
       db.commit()
       F=open("D:/MM/assets/"+filename,"wb")
       for chunk in producticon.chunks():
           F.write(chunk)
       F.close()

       db.close()
       return render(request, "ProductInterface.html",{'msg':'Record Successfully Submitted'})

    except Exception as e:
        print("Error:",e)
        return render(request, "ProductInterface.html",{'msg':'Record Submission Failed'})


def DisplayAllProduct(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid),(select SC.subcategoryname from subcategories SC where SC.subcategoryid=P.subcategoryid) from products P"
        cmd.execute(q)
        rows=cmd.fetchall()

        db.close()
        return render(request,"DisplayAllProduct.html",{'rows':rows})
    except Exception as e:
        return render(request, "DisplayAllProduct.html", {'rows': []})

def DisplayProductById(request):
    try:
        pid=request.GET['pid']
        db,cmd=Pool.ConnectionPool()
        q = "select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid),(select sc.subcategoryname from subcategories sc where sc.subcategoryid=p.subcategoryid) from products p where productid={}".format(pid)
        cmd.execute(q)
        row=cmd.fetchone()

        db.close()
        return render(request,"DisplayProductById.html",{'row':row})
    except Exception as e:
        print("error:",e)
        return render(request, "DisplayProductById.html", {'row': []})

def EditDeleteProductRecord(request):
    btn=request.GET['btn']
    pid = request.GET['pid']
    if(btn=="Edit"):
      # cid = request.GET['cid']
      # scid = request.GET['scid']
      cid = request.GET['categoryid']
      scid = request.GET['subcategoryid']

      productname = request.GET['productname']
      pdescription = request.GET['pdescription']
      try:
        db,cmd=Pool.ConnectionPool()
        q = "update products set categoryid={},subcategoryid={},productname='{}',pdescription='{}' where productid={} ".format(cid,scid,productname,pdescription,pid)
        cmd.execute(q)
        db.commit()

        db.close()
        return DisplayAllProduct(request)
      except Exception as e:
        print("error:",e)
        return DisplayAllProduct(request)
    elif(btn=="Delete"):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "Delete from products where productid={}".format(pid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllProduct(request)
        except Exception as e:
            print("error:", e)
            return DisplayAllProduct(request)

def EditProductIcon(request):
    try:
        pid=request.GET['pid']
        productname=request.GET['productname']
        producticon=request.GET['producticon']
        row=[pid,productname,producticon]
        return render(request,"EditProductIcon.html",{'row':row})
    except Exception as e:
        print("error:",e)
        return render(request,"EditProductIcon.html",{'row':[]})

def SaveEditIcon(request):
    try:
       pid=request.POST['pid']
       oldpicture = request.POST['oldpicture']
       producticon=request.FILES['producticon']
       filename=str(uuid.uuid4())+producticon.name[producticon.name.rfind('.'):]
       password="".join(random.sample(['1','a','4','x','6','66','#','@'],k=7))
       db, cmd = Pool.ConnectionPool()
       q="update products set producticon='{}' where productid={}".format(filename,pid)

       cmd.execute(q)
       db.commit()
       F=open("D:/MM/assets/"+filename,"wb")
       for chunk in producticon.chunks():
           F.write(chunk)
       F.close()

       db.close()
       os.remove("D:/MM/assets/"+oldpicture)
       return DisplayAllProduct(request)
    except Exception as e:
       print("error:", e)
       return DisplayAllProduct(request)

def GetProductJson(request):
 try:
  db,cmd=Pool.ConnectionPool()
  scid=request.GET['scid']
  q="select * from products where subcategoryid={}".format(scid)
  cmd.execute(q)
  rows=cmd.fetchall()
  db.close()
  return JsonResponse(rows,safe=False)

 except Exception as e:
  print(e)
  return JsonResponse([],safe=False)

