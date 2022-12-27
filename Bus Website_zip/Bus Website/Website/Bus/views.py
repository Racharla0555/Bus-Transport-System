from django.shortcuts import render , redirect
from Bus.models import Signup , Contacts , Update
# from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate , logout , login 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from Bus.decorators import *
from django.contrib.auth.models import Group


# admin username- Pavan
# admin password - 1234

# user username - rahul
# user passowrd - Hello123$

# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    # global St_name
    if (request.method) == 'POST':
        fullname = request.POST.get('fullname')
        Mnumber = request.POST.get('phone')
        Rollno = request.POST.get('rollno')
        Email = request.POST.get('Email')
        Branch_Name = request.POST.get('Branch')
        Rt_number = request.POST.get('Root Number')
        St_name = request.POST.get('Location')
        
        signup = Signup(fname=fullname , number=Mnumber , rollno=Rollno , email=Email , Branch=Branch_Name , rt_number=Rt_number , st_name=St_name)
        a=Signup.objects.filter(rt_number=Rt_number).count()
        if(a<=40):
            signup.save()
            
            return render(request,'success.html')
        else:
            
            return render(request,'signup_fail.html')
    return render(request, 'signup.html')


def success(request):
    return render(request,'success.html')


def fail(request):
    return render(request,'signup_fail.html')



def COntact(request):
    if (request.method) =="POST":
        name=request.POST.get('name')
        Hallticket=request.POST.get('Hallticket')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        Contact = Contacts(name = name , Hallticket = Hallticket , email = email , desc = desc)
        Contact.save()
        return render(request,'contact_successful.html')

    return render(request,'contact.html')




def about(request):
    return render(request,'about.html')

@user_passes_test(lambda u:u.is_superuser)
# @allowed_users(allowed_roles=['admin'])
# @admin_only
def admin_viewpage(request):
    return render(request,'admin_viewpage.html')


def admin_login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(username = username , password = password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
            # return redirect('Admin_viewpage')
                return redirect('/viewpage')
            else:
                login(request,user)
                return redirect('/stupdates')
        
    return render(request,'admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect('/login')


@user_passes_test(lambda u:u.is_superuser)
@allowed_users(allowed_roles=['admin'])
def students(request):
    
    stud_list1 = Signup.objects.filter(rt_number=1)
    a=40 - Signup.objects.filter(rt_number=1).count()
    
    stud_list2 = Signup.objects.filter(rt_number=2)
    b=40 - Signup.objects.filter(rt_number=2).count()
    
    stud_list3 = Signup.objects.filter(rt_number=3)
    c=40 - Signup.objects.filter(rt_number=3).count()
    
    stud_list4 = Signup.objects.filter(rt_number=4)
    d=40 - Signup.objects.filter(rt_number=4).count()
    
    stud_list5 = Signup.objects.filter(rt_number=5)
    e=40 - Signup.objects.filter(rt_number=5).count()
    
    stud_list6 = Signup.objects.filter(rt_number=6)
    f=40 - Signup.objects.filter(rt_number=6).count()
    
    stud_list7 = Signup.objects.filter(rt_number=7)
    g=40 - Signup.objects.filter(rt_number=7).count()
    
    stud_list8 = Signup.objects.filter(rt_number=8)
    h=40 - Signup.objects.filter(rt_number=8).count()
    
    stud_list9 = Signup.objects.filter(rt_number=9)
    i=40 - Signup.objects.filter(rt_number=9).count()
    
    stud_list10 = Signup.objects.filter(rt_number=10)
    j=40 - Signup.objects.filter(rt_number=10).count()
    return render(request,'admin_students.html',{'stud_list1': stud_list1,'stud_list2': stud_list2,'stud_list3': stud_list3,'stud_list4': stud_list4,'stud_list5': stud_list5,'stud_list6': stud_list6,'stud_list7': stud_list7,'stud_list8': stud_list8,'stud_list9': stud_list9,'stud_list10': stud_list10,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j})

@user_passes_test(lambda u:u.is_superuser)
@allowed_users(allowed_roles=['admin'])
def query(request):
    query=Contacts.objects.all()
    return render(request,'admin_query.html',{'query':query})

def query_success(request):
    return render(request,'contact_successful.html')

@user_passes_test(lambda u:u.is_superuser)
def adminupdate(request):
    if request.method =='POST':
        desc = request.POST.get('updates')
        Updates=Update(desc = desc)
        Updates.save()
    return render(request,'admin_updates.html')

@allowed_users(allowed_roles=['students'])
def studentupdate(request):
    updates=Update.objects.all()
    return render(request,'student_updates.html',{'updates':updates})

def studsignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,email=email,password=password)
        group = Group.objects.get(name = 'students')
        user.groups.add(group)
    return render(request,'student_signup.html') 

