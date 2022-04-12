"""MM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import EmployeeView
from.import Statecityview
from.import CategoryView
from.import SubCategoryView
from.import ProductView
from.import AdminView
from.import FinalProductView
from.import PurchaseView
from.import IssueView




urlpatterns = [
    path('admin/', admin.site.urls),
    # Admin login
    path('adminlogin/', AdminView.AdminLogin),
    path('checkadminlogin', AdminView.CheckAdminLogin),
    path('adminlogout',AdminView.AdminLogout),

    #Employee Login
    path('employeelogin', EmployeeView.EmployeeLogin),
    path('checkemployeelogin', EmployeeView.CheckEmployeeLogin),
    path('employeelogout',EmployeeView.EmployeeLogout),
    #Employee
    path('employeeinterface/',EmployeeView.EmployeeInterface),
    path('employeesubmit',EmployeeView.EmployeeSubmit),
    path('displayall/displayemployeebyid/', EmployeeView.DisplayById),
    path('displayall/', EmployeeView.DisplayAll),
    path('editdeleterecord/', EmployeeView.EditDeleteRecord),
    path('displayall/editemployeepicture/', EmployeeView.EditEmployeePicture),
    path('saveeditpicture', EmployeeView.SaveEditPicture),

    path('fetchallstates/', Statecityview.FetchAllStates),
    path('fetchallcities/', Statecityview.FetchAllCities),

    #Categories
    path('category/',CategoryView.Category),
    path('categorysubmit',CategoryView.CategorySubmit),
    path('displayallcategory/', CategoryView.DisplayAllCategory),
    # path('displayallcategory/displaycategorybyid/', CategoryView.DisplayCategoryById),
    path('editdeletecategoryrecord/', CategoryView.EditDeleteCategoryRecord),
    path('displayallcategory/editcategoryicon/', CategoryView.EditCategoryIcon),
    path('saveeditcategoryicon', CategoryView.SaveEditIcon),

    path('getcategoryjson',CategoryView.GetCategoryJson),

    #Subcategories


    path('subcategoryinterface/', SubCategoryView.SubCategoryInterface),
    path('subcategorysubmit',SubCategoryView.SubCategorySubmit),
    path('displayallsubcategory/', SubCategoryView.DisplayAllSubcategory),
    path('displayallsubcategory/displaysubcategorybyid/', SubCategoryView.DisplaySubcategoryById),
    path('editdeletesubcategoryrecord/', SubCategoryView.EditDeleteSubCategoryRecord),
    path('displayallsubcategory/editsubcategoryicon/',SubCategoryView.EditSubcategoryIcon),
    path('saveeditsubcategoryicon', SubCategoryView.SaveEditIcon),
    path('getsubcategoryjson',SubCategoryView.GetSubCategoryJson),

    #product
    path('productinterface/', ProductView.ProductInterface),
    path('productsubmit', ProductView.ProductSubmit),
    path('displayallproduct', ProductView.DisplayAllProduct),
    path('displayproductbyid/', ProductView.DisplayProductById),
    path('editdeleteproductrecord', ProductView.EditDeleteProductRecord),
    path('editproducticon/', ProductView.EditProductIcon),
    path('saveeditproducticon', ProductView.SaveEditIcon),
    path('getproductjson/',ProductView.GetProductJson),

    # Final product
    path('finalproductinterface/',FinalProductView.FinalProductInterface),
    path('finalproductsubmit',FinalProductView.FinalProductSubmit),
    path('displayallfinalproduct',FinalProductView.DisplayAllFinalProduct),
    path('getfinalproductjson', FinalProductView.GetFinalProductJson),
    path('displayfinalproductbyidjson/', FinalProductView.DisplayFinalProductByIdJson),
    path('displayfinalproductalljson/', FinalProductView.DisplayFinalProductAllJson),
    path('displayupdatedstock/', FinalProductView.DisplayUpdatedStock),

    #Purchase
    path('purchaseinterface/',PurchaseView.PurchaseInterface),
    path('purchaseproductsubmit',PurchaseView.PurchaseProductSubmit),

    #Issue
    path('issueinterface/',IssueView.IssueInterface),

]
