from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from somgr.models import Project
from somgr import *

@login_required(login_url="/somgr/login.html")
def index(request):
    latest_project_list = Project.objects.order_by("name")[:10]
    context = {"page_title":page_title, "latest_project_list": latest_project_list}
    return render(request, "index.html", context)

@login_required(login_url="/somgr/login.html")
def project(request, project_id):
    if request.method == "GET": 
        context ={"page_title":page_title}
        return render(request, "signoffList.html", context)

    if request.method == "POST": 
        project = get_object_or_404(Project, pk=project_id)
        selected_signoff = project.signoff_set.get(pk=request.POST["soteam"])
        selected_signoff.save()
        context = {"page_title":page_title}
        return render(request, "signoffList.html", context)  
    
def login(request):
    if request.method == "GET": 
        context ={"page_title":page_title}
        return render(request, "login.html", context)

    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("OK")
        else:
            return render(request,"userlogin.html",{
                "message":"Invalid Credentials"
            })
    return render(request,"userlogin.html")

def logout_page(request):
    return render(request,'userlogin.html',{
        'message':"Logged out"
    })
