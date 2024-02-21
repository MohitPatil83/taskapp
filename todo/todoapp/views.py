from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import TaskList
from django.db.models import Q


def home(request):
    #print("user",request.user.is_authenticated)
    if request.user.is_authenticated:

        q1=Q(is_activate=1)
        q2=Q(user_id=request.user.id)

        t=TaskList.objects.filter(q1 & q2)
    
        context={}
        context['data']=t
        return render(request,'todoapp/dashboard.html',context)
    else:
        return redirect('/authapp/login')


def about(request):


    return HttpResponse("Hey this is About !!!!!")

def contact(request):


    return HttpResponse("Hey this is contact !!!!!")

def add_task(request):

    print("Method type:",request.method)
    if request.method=="POST":
        t=request.POST['title']
        d=request.POST['det']
        dt=request.POST['duedt']
        #print("title:",t)
        #print("Details:",d)
        #print("Date:",dt)
        t=TaskList.objects.create(title=t,detail=d,due_dt=dt,user_id=request.user)
        t.save()
        
        #return HttpResponse("Task created Successfully")
        return redirect('/home')

    else:
        print("In else section")
        

        return render(request,'todoapp/addtask.html')

def dtl(request):
    context={}
    context['a']=70
    context['user']="Mohit"
    context['b']=50
    context['l']=[10,20,30,40,50,60]
    return render(request,'todoapp/dashboard.html',context)
# Create your views here.

def delete_task(request,rid):
    #t=TaskList.objects.get(id=rid)#select * from tablename where id=3
    #t.delete()
    #print("Id to be  deleted:",rid)
    #print(t)
    #return HttpResponse("Id to be deleted:"+rid)
    t=TaskList.objects.filter(id=rid)
    t.update(is_activate=0)
    return redirect('/home')
    

def edit_task(request,rid):
    #print("Id to be Edited",rid) 

    #return HttpResponse("Id to be edited"+rid)
    if request.method=="POST":
        ut=request.POST['title']
        ud=request.POST['det']
        udt=request.POST['duedt']
        print("updated title:",ut)
        print("updated Details:",ud)
        print("updated Date:",udt)
        t=TaskList.objects.filter(id=rid)
        t.update(title=ut,detail=ud,due_dt=udt)
        return redirect("/home")
        
    else:
        t=TaskList.objects.get(id=rid)
        context={}
        context['data']=t
        return render(request,'todoapp/editform.html',context)
    
def mark_completed(request,rid):
    t=TaskList.objects.filter(id=rid)
    t.update(is_completed=1)
    return redirect('/home')