from django.shortcuts import render
from .utils import *
import random
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password ,check_password
import uuid
from django.core.paginator import Page, Paginator
import datetime
from itertools import chain

# Create your views here.
#Login operation in login method
def login(request):
    if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        #check user is exist or not 
        Check_User_Exist=All_User.objects.filter(Email=Email)
        if Check_User_Exist:
            #All User object
            User_obj=All_User.objects.get(Email=Email)
            if check_password(Password,User_obj.password)==True:
                #create a session 
                request.session['email']=Email
                return render(request,'shop_admin\Home.html')
            else:
                wrong='wrong password pleace check'.title()
                return render(request,'shop_admin\login.html',{'wrong':wrong})
        elif Email=='' or Password=='':
            wrong='pleace Enter username or password '.title()
            return render(request,'shop_admin\login.html',{'wrong':wrong})
        else:
            wrong='username or password wrong pleace login check'.title()
            return render(request,'shop_admin\login.html',{'wrong':wrong})
    elif request.method=='GET':
        if 'email' in request.session:
            return render(request,'shop_admin\Home.html')
        else:
            return render(request,'shop_admin\login.html')
    else:
        return render(request,'shop_admin\login.html')

#Registration operation in Registration method
def Registration(request):
    if request.method=='POST':
        First_Name=request.POST['first_name']
        Last_Name=request.POST['last_name']
        Email=request.POST['email']
        Password=request.POST['password']
        Password_Confirmation=request.POST['password_confirmation']
        #check password and confiemations password is same or different
        if Password==Password_Confirmation:
            #check user is exist or not 
            Check_User_Exist=All_User.objects.filter(Email=Email)
            if Check_User_Exist:
                Wrong_Password='user already exists '.title()
                return render(request,'shop_admin\Registration.html',{'Wrong_Password':Wrong_Password})
            else:
                Email_Token=random.randint(111111,999999)
                Token_id=str(uuid.uuid4())
                varification_token=Verification.objects.create(Token=Email_Token,Token_id=Token_id)
                #Send Email User Registration
                try:
                    sendmail("For verification via Email ","shop_admin/SendOTP.html",Email,{'Firstname':First_Name,'Lastname':Last_Name,'OTP':Email_Token})
                except Exception as E:
                    Wrong_Password='wrong Email id '.title()
                    return render(request,'shop_admin\Registration.html',{'Wrong_Password':Wrong_Password})
                user_detail={
                    'First_Name':First_Name,
                    'Last_Name':Last_Name,
                    'Email':Email,
                    'Password':Password,
                    'Token_id':Token_id
                }
                return render(request,'shop_admin\OTP_Page.html',{'user_detail':user_detail})
        else:
            #if password and confiemations password is different
            Wrong_Password='password and confiemations is different Pleace try again'.title()
            return render(request,'shop_admin\Registration.html',{'Wrong_Password':Wrong_Password})
    elif request.method =='GET':
        if 'email' in request.session:
            return render(request,'shop_admin\Home.html')
        else:
            return render(request,'shop_admin\Registration.html')
    else:
        return render(request,'shop_admin\Registration.html')

#OTP Verification  operation in OTPVerification method
def OTPVerification(request):
    if request.method=='POST':
        First_Name=request.POST['first_name']
        Last_Name=request.POST['last_name']
        Email=request.POST['email']
        Password=request.POST['password']
        OTP=request.POST['OTP']
        Token_id=request.POST['Token_id']
        verifiy=Verification.objects.filter(Token=OTP,Token_id=Token_id)
        if verifiy:
            Password=make_password(Password)
            All_User.objects.create(First_Name=First_Name,Last_Name=Last_Name,Email=Email,password=Password)
            wrong='Account create successfully pleaces loging'.title()
            return render(request,'shop_admin\login.html',{'wrong':wrong})
        else:
            #if password and confiemations password is different
            Wrong_Otp='wrong otp '.title()
            return render(request,'shop_admin\Registration.html',{'Wrong_Password':Wrong_Otp})
    elif request.method=='GET':
        return render(request,'shop_admin\Registration.html')
    else:
        return render(request,'shop_admin\Registration.html')

# Add product and home view operations in Home method
def Home(request):
    #Add New product 
    if request.method=='POST':
        ProductName=request.POST['ProductName']
        Food_Category=request.POST['category']
        DueDate=request.POST['DueDate']
        Email_id=request.session['email']
        ProductDetails.objects.create(Email_id=Email_id,ProductName=ProductName,ProductCategory=Food_Category,ProductDueDate=DueDate)
        return render(request,'shop_admin\Home.html')
    elif request.method=='GET':
        if 'email' in request.session:
            return render(request,'shop_admin\Home.html')
        else:
            return render(request,'shop_admin\Registration.html')
    else:
        return render(request,'shop_admin\login.html')

#logout operations in logout method
def Logout(request):
    if request.method =='GET':
        if 'email' in request.session:
            del request.session['email']
            return render(request,'shop_admin\login.html')
        else:
            return render(request,'shop_admin\login.html')
    else:
        return render(request,'shop_admin\login.html')

#Product Details view in Product_Details page used this method
def Product_Details(request):
    if request.method=='GET':
        if 'email' in request.session:
            Email_id=request.session['email']
            Product_obj=ProductDetails.objects.filter(Email_id=Email_id)
            return render(request,'shop_admin\ProductDetails.html',{'Product_obj':Product_obj})
        else:
            return render(request,'shop_admin\login.html')
    else:
        return render(request,'shop_admin\login.html')

#UpdateProduct  operations in operations method
def UpdateProduct(request,pk):
    if request.method=='GET':
        if 'email' in request.session:
            update_obj=ProductDetails.objects.filter(id=pk)
            if update_obj:
                return render(request,'shop_admin/UpdateProduct.html',{'update_obj':update_obj})
            else:
                return render(request,'shop_admin\Home.html')
        else:
            return render(request,'shop_admin\login.html')
    elif request.method=='POST':
        ProductName=request.POST['ProductName']
        product_category=request.POST['category']
        update_obj=ProductDetails.objects.get(id=pk)
        update_obj.ProductName=ProductName
        update_obj.ProductCategory=product_category
        update_obj.save()
        Email_id=request.session['email']
        Product_obj=ProductDetails.objects.filter(Email_id=Email_id)
        return render(request,'shop_admin\ProductDetails.html',{'Product_obj':Product_obj})
    else:
        return render(request,'shop_admin\login.html')
#Delete operations method in Delete method
def Delete(request,pk):
    if request.method=='GET':
        if 'email' in request.session:
            delete_obj=ProductDetails.objects.filter(id=pk)
            if delete_obj:
                delete_obj=ProductDetails.objects.get(id=pk)
                delete_obj.delete()
                Email_id=request.session['email']
                Product_obj=ProductDetails.objects.filter(Email_id=Email_id)
                return render(request,'shop_admin\ProductDetails.html',{'Product_obj':Product_obj})
            else:
                return render(request,'shop_admin\Home.html')
        else:
            return render(request,'shop_admin\login.html')
    else:
        return render(request,'shop_admin\login.html')
#search all product used search method
def search(request):
    if request.method=='POST':
        ProductName=request.POST['ProductName']
        productCategory=request.POST['category']
        DueDate=request.POST['DueDate']
        Email_id=request.session['email']
        #product search used for query product name category due date
        if DueDate!='':
            #query run with due date
            search=ProductDetails.objects.raw(f"""select * from public.shop_admin_productdetails where "Email_id"='{Email_id}' and "ProductName" like '{ProductName}' or "ProductCategory" like '{productCategory}' or "ProductDueDate"='{DueDate}'""")
        if DueDate=="":
            #query run without due date
            search=ProductDetails.objects.raw(f"""select * from public.shop_admin_productdetails where "Email_id"='{Email_id}' and "ProductName" like '{ProductName}' or "ProductCategory" like '{productCategory}'""")
        return render(request,'shop_admin\ProductDetails.html',{'Product_obj':search})
    else:
        if 'email' in request.session:
            return render(request,'shop_admin\Home.html')
        else:
            return render(request,'shop_admin\login.html')
