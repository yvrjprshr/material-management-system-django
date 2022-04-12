from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
import uuid
import os
import random

def SubCategoryInterface(request):
    return render(request,"SubCategoryInterface.html")

def SubCategorySubmit(request):
    try:
       categoryid=request.POST['categoryid']
       subcategoryname=request.POST['subcategoryname']
       scdescription = request.POST['scdescription']
       subcategoryicon =request.FILES['subcategoryicon']

       filename=str(uuid.uuid4())+subcategoryicon.name[subcategoryicon.name.rfind('.'):]
       db, cmd = Pool.ConnectionPool()
       q="insert into subcategories(categoryid,subcategoryname,scdescription,subcategoryicon)values({},'{}','{}','{}')".format(categoryid,subcategoryname,scdescription,filename)
       cmd.execute(q)
       db.commit()
       F=open("D:/MM/assets/"+filename,"wb")
       for chunk in subcategoryicon.chunks():
           F.write(chunk)
       F.close()

       db.close()
       return render(request, "SubCategoryInterface.html",{'msg':'Record Successfully Submitted'})

    except Exception as e:
        print("Error:",e)
        return render(request, "SubCategoryInterface.html",{'msg':'Record Submission Failed'})


def DisplayAllSubcategory(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from subcategories"
        cmd.execute(q)
        rows=cmd.fetchall()

        db.close()
        return render(request,"DisplayAllSubCategory.html",{'rows':rows})
    except Exception as e:
        return render(request, "DisplayAllSubCategory.html", {'rows': []})

def DisplaySubcategoryById(request):
    try:
        scid=request.GET['scid']
        db,cmd=Pool.ConnectionPool()
        q="select sc.*,(select c.categoryname from categories c where c.categoryid=sc.categoryid) from subcategories sc where subcategoryid='{}'".format(scid)

        cmd.execute(q)
        row=cmd.fetchone()

        db.close()
        return render(request,"DisplaySubcategoryById.html",{'row':row})
    except Exception as e:
        print("error:",e)
        return render(request, "DisplaySubcategoryById.html", {'row': []})

def EditDeleteSubCategoryRecord(request):
    btn=request.GET['btn']
    scid = request.GET['scid']
    if(btn=="Edit"):
     cid = request.GET['cid']
     subcategoryname= request.GET['subcategoryname']
     scdescription = request.GET['scdescription']
     try:
        db,cmd=Pool.ConnectionPool()
        q = "update subcategories set categoryid={}, subcategoryname='{}', scdescription='{}'  where subcategoryid={} ".format(cid,subcategoryname,scdescription,scid)
        cmd.execute(q)
        db.commit()

        db.close()
        return DisplayAllSubcategory(request)
     except Exception as e:
        print("error:",e)
        return DisplayAllSubcategory(request)
    elif(btn=="Delete"):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "Delete from categories where subcategoryid={}".format(scid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllSubcategory(request)
        except Exception as e:
            print("error:", e)
            return DisplayAllSubcategory(request)

def EditSubcategoryIcon(request):
    try:
        scid=request.GET['scid']
        subcategoryname=request.GET['subcategoryname']
        subcategoryicon=request.GET['subcategoryicon']
        row=[scid,subcategoryname,subcategoryicon]
        return render(request,"EditSubCategoryIcon.html",{'row':row})
    except Exception as e:
        print("error:",e)
        return render(request,"EditSubCategoryIcon.html",{'row':[]})

def SaveEditIcon(request):
    try:
       scid=request.POST['scid']
       oldpicture = request.POST['oldpicture']
       subcategoryicon=request.FILES['subcategoryicon']
       filename=str(uuid.uuid4())+subcategoryicon.name[subcategoryicon.name.rfind('.'):]
       password="".join(random.sample(['1','a','4','x','6','66','#','@'],k=7))
       db, cmd = Pool.ConnectionPool()
       q="update categories set subcategoryicon='{}' where subcategoryid={}".format(filename,scid)

       cmd.execute(q)
       db.commit()
       F=open("D:/MM/assets/"+filename,"wb")
       for chunk in subcategoryicon.chunks():
           F.write(chunk)
       F.close()

       db.close()
       os.remove("D:/MM/assets/"+oldpicture)
       return DisplayAllSubcategory(request)
    except Exception as e:
       print("error:", e)
       return DisplayAllSubcategory(request)


def GetSubCategoryJson(request):
 try:
  db,cmd=Pool.ConnectionPool()
  cid=request.GET['cid']
  q="select * from subcategories where categoryid={}".format(cid)
  cmd.execute(q)
  rows=cmd.fetchall()
  db.close()
  return JsonResponse(rows,safe=False)

 except Exception as e:
  print(e)
  return JsonResponse([],safe=False)



