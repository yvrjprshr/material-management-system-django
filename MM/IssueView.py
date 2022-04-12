from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
import uuid
import os
import random

def IssueInterface(request):
    result=request.session['EMPLOYEE']
    return render(request,"IssueInterface.html",{'result':result})
def IssueProductSubmit(request):
    try:
       employeeid=request.POST['employeeid']
       categoryid = request.POST['categoryid']
       subcategoryid = request.POST['subcategoryid']
       productid= request.POST['productid']
       finalproductid = request.POST['finalproductid']
       demandemployeeid = request.POST['demandemployeeid']
       dateissue = request.POST['dateissue']
       qtyissue= request.POST['dateissue']
       remark=request.POST['remark']


       db, cmd = Pool.ConnectionPool()
       q="insert into issue (employeeid,categoryid, subcategoryid, productid, finalproductid, demand_employeeid, dateissue, qtyissue, remark)values({},{},{},{},{},{},'{}',{},'{}' )".format(employeeid,categoryid, subcategoryid, productid, finalproductid, demandemployeeid, dateissue, qtyissue, remark)
       cmd.execute(q)

       #Update Stocks
       q="update finalproducts set stock=stock-{} where finalproductid={}".format(qtyissue,finalproductid)
       cmd.execute(q)
       db.commit()
       return render(request, "IssueInterface.html",{'msg':'Record Submission Succesfully'})



    except Exception as e:
        print("Error:",e)
        return render(request, "PurchaseInterface.html",{'msg':'Record Submission Failed'})
