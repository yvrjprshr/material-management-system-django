from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
import uuid
import os
import random

def Category(request):
    return render(request,"Category.html")
def CategorySubmit(request):
    try:
       categoryname=request.POST['categoryname']
       categoryicon =request.FILES['categoryicon']

       filename=str(uuid.uuid4())+categoryicon.name[categoryicon.name.rfind('.'):]
       db, cmd = Pool.ConnectionPool()
       q="insert into categories(categoryname,categoryicon)values('{}','{}')".format(categoryname,filename)
       cmd.execute(q)
       db.commit()
       F=open("D:/MM/assets/"+filename,"wb")
       for chunk in categoryicon.chunks():
           F.write(chunk)
       F.close()

       db.close()
       return render(request, "Category.html",{'msg':'Record Successfully Submitted'})

    except Exception as e:
        print("Error:",e)
        return render(request, "Category.html",{'msg':'Record Submission Failed'})


def DisplayAllCategory(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()

        db.close()
        return render(request,"DisplayAllCategory.html",{'rows':rows})
    except Exception as e:
        return render(request, "DisplayAllCategory.html", {'rows': []})

# def DisplayCategoryById(request):
#     try:
#         cid=request.GET['cid']
#         db,cmd=Pool.ConnectionPool()
#         q="select * from categories where categoryid='{}'".format(cid)
#         cmd.execute(q)
#         row=cmd.fetchone()
#
#         db.close()
#         return render(request,"DisplayCategoryById.html",{'row':row})
#     except Exception as e:
#         print("error:",e)
#         return render(request, "DisplayCategoryById.html", {'row': []})

def EditDeleteCategoryRecord(request):
    btn=request.GET['btn']
    cid = request.GET['cid']
    if(btn=="Edit"):
      categoryname = request.GET['categoryname']
      try:
        db,cmd=Pool.ConnectionPool()
        q = "update categories set categoryname='{}' where categoryid={} ".format(categoryname,cid)
        print(q)
        cmd.execute(q)
        db.commit()

        db.close()
        return DisplayAllCategory(request)
      except Exception as e:
        print("error:",e)
        return DisplayAllCategory(request)
    elif(btn=="Delete"):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "Delete from categories where categoryid={}".format(cid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllCategory(request)
        except Exception as e:
            print("error:", e)
            return DisplayAllCategory(request)

def EditCategoryIcon(request):
    try:
        cid=request.GET['cid']
        categoryname=request.GET['categoryname']
        categoryicon=request.GET['categoryicon']
        row=[cid,categoryname,categoryicon]
        return render(request,"EditCategoryIcon.html",{'row':row})
    except Exception as e:
        print("error:",e)
        return render(request,"EditCategoryIcon.html",{'row':[]})

def SaveEditIcon(request):
    try:
       cid=request.POST['cid']
       oldpicture = request.POST['oldpicture']
       categoryicon=request.FILES['categoryicon']
       filename=str(uuid.uuid4())+categoryicon.name[categoryicon.name.rfind('.'):]
       password="".join(random.sample(['1','a','4','x','6','66','#','@'],k=7))
       db, cmd = Pool.ConnectionPool()
       q="update categories set categoryicon='{}' where categoryid={}".format(filename,cid)

       cmd.execute(q)
       db.commit()
       F=open("D:/MM/assets/"+filename,"wb")
       for chunk in categoryicon.chunks():
           F.write(chunk)
       F.close()

       db.close()
       os.remove("D:/MM/assets/"+oldpicture)
       return DisplayAllCategory(request)
    except Exception as e:
       print("error:", e)
       return DisplayAllCategory(request)


def GetCategoryJson(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()

        db.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)


