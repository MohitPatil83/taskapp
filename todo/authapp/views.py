from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_register(request):
    if request.method == "POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']
        context={}
        if uname=="" or upass=="" or ucpass=="" or uemail=="":
            context['errmsg']="fields cannot be balnk"
            return render(request,'authapp/register.html',context)
        elif upass != ucpass:
            context['errmsg']="Password And Confirm Password missmatch"
            return render(request,'authapp/register.html',context)
        else:

            t=User.objects.create(username=uname,email=uemail)
            t.set_password(upass)
            t.save()
            context['success']="Account created Successfully Please Login"
            return render(request,'authapp/register.html',context)
    else:

        return render(request,'authapp/register.html')
    
def user_login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        print("Username",uname)
        print("Password",upass)
        u=authenticate(username=uname,password=upass)
        #print("Id",u.id)
        #print("Username",u.username)
        #print("Password",u.password)
        #print("Email",u.email)
        #print("Superuser",u.is_superuser)
        #print("Date",u.date_joined)
        #print("User object:",u)
        if u is not None:
            login(request,u)
            return redirect('/home')

        else:
            context={}
            context['errmsg']="Invalid username And Passowrd"
            #return HttpResponse("Invalid username")
            return render(request,'authapp/login.html',context)

    else:
        return render(request,'authapp/login.html')
def user_logout(request):
    logout(request)
    return redirect('/authapp/login')