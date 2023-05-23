from django.shortcuts import render
from jobsite.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
import datetime as dt


def Services(request):
    return render(request,"services.html")
def Portfolio(request):
    return render(request,"portfolio.html")
def About(request):
    all_data = Postjob.objects.all()
    count = all_data.count()
    return render(request,"about.html",{"count":count})

def joblisting(request):
    all_data = Postjob.objects.all()
    count = all_data.count()
    return render(request,"job-listings.html",{"key1": all_data, "count":count})

def Home(request):
    all_data = Postjob.objects.all()
    count = all_data.count()
    return render(request,"Home.html",{"key1": all_data, "count":count})

def Jobdetails(request,pk):
    updata = Postjob.objects.get(id=pk)
    all_data = Postjob.objects.all()
    count = all_data.count()
    return render(request, 'job-single.html', {'key2': updata,'key1':all_data,'count':count})

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("Home.html")
        else:
            messages.error(request, "Invalid User Name or Password")
            return redirect("/login")
    return render(request, "login.html")


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success You can Login Now..!")
            return redirect('/login')
        else:
            messages.error(request, "Form Is Not Valid")
            return render(request, "register.html", {'form': form})
    return render(request, "register.html", {'form': form})

def postjob(request):
    if request.method == 'POST':
        email= request.POST['email']
        job_Title= request.POST['job_Title']
        location= request.POST['location']
        job_Region = request.POST['job_Region']
        job_Type=  request.POST['job_Type']
        job_Description= request.POST['job_Description']
        company_Name= request.POST['company_Name']
        company_Description= request.POST['company_Description']
        website= request.POST['website']
        facebook_Username = request.POST['facebook_Username']
        twitter_Username = request.POST['twitter_Username']
        linkedin_Username = request.POST['linkedin_Username']
        
        new = Postjob.objects.create(Email=email,Job_Title=job_Title,Location=location,Job_Region=job_Region,Job_Type=job_Type,Job_Description=job_Description,
            Company_Name=company_Name,Company_Description=company_Description,Website=website,Facebook_Username=facebook_Username,Twitter_Username=twitter_Username,
            Linkedin_Username=linkedin_Username)
    return render(request,"post-job.html")

def Contact(request):
    if request.method == 'POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        subject = request.POST['subject']
        message=  request.POST['message']
        
        new = Contacts.objects.create(First_name=fname,Last_name=lname,Email=email,Subject=subject,Message=message)
        return render(request,"contact.html")
    return render(request,"contact.html")

def jobsearch(request):
        return render(request,"Home.html")