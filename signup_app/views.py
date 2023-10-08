from django.shortcuts import render,redirect
from .models import *


def signup_insert_page(request):
    return render(request,"app/signup.html")

def signup_upload_page(request):
    if request.method=='POST':
        usern=request.POST['user']
        usermob=request.POST['mobile']
        userem=request.POST['email']
        userpass=request.POST['password']
        cuserpass=request.POST['cpassword']
        user_data=signupdata.objects.filter(Email=userem)
        if user_data:
            message="user already exists"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if cuserpass==userpass:
                message="user successfully signup and do login"
                database=signupdata.objects.create(UserName=usern,MobileNo=usermob,Email=userem,Password=userpass)
                database.save()
                return render(request,"app/login.html",{'msg':message})
            else:
                message="password doesnot matching"
                return render(request,"app/signup.html",{'msg':message})
        
       

def signup_login_page(request):
    if request.method=="POST":
        email2=request.POST['email']
        password2=request.POST['password']
        user=signupdata.objects.get(Email=email2)
        if user:
            if user.Password==password2:
                request.session['username']=user.UserName
                request.session['usermobile']=user.MobileNo
                request.session['useremail']=user.Email
                request.session['userpassword']=user.Password
                return render(request,"app/show.html")
            else:
                message="password doesnot match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message="user does not exists do signup"
            return render(request,"app/signup.html",{'msg':message})    
        