from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse
from somgr.models import Project
from somgr import *

def index(request):
    latest_project_list = Project.objects.order_by("name")[:10]
    context = {"page_title":page_title, "latest_project_list": latest_project_list}
    return render(request, "index.html", context)

def signoff(request, project_id):
    if request.method == "GET": 
        context ={"page_title":page_title}
        return render(request, "signoff-form.html", context)

    if request.method == "POST": 
        context = {"page_title":page_title}
        return render(request, "signoff-list.html", context)  
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request,"userlogin.html",{
                "message":"Invalid Credentials"
            })
    return render(request,"userlogin.html")

def logout_page(request):
    return render(request,'userlogin.html',{
        'message':"Logged out"
    })
