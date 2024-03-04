from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from somgr.models import Project, Signoff
from somgr import *

@login_required(login_url="/somgr/login")
def index(request):
    latest_project_list = Project.objects.order_by("name")[:10]
    context = {"page_title":page_title, "latest_project_list": latest_project_list}
    return render(request, "index.html", context)

@login_required(login_url="/somgr/login")
def project(request, project_id):

    if request.method == "GET": 
        context ={"page_title":page_title, "project": Project.objects.get(id=project_id)}
        return render(request, "signoffList.html", context)

    if request.method == "POST":
        try:
            signoff = Signoff.objects.get(project_id=project_id, soteam=request.POST['soteam'])
            signoff.soby = "william"
            signoff.sodate = timezone.now()
            signoff.save()
        except Signoff.DoesNotExist:
            return render(request, "signoffList.html", context)  

        context ={"page_title":page_title, "project": Project.objects.get(id=project_id)}
     
        return render(request, "signoffList.html", context)  
    
def login(request):
    if request.method == "GET": 
        context ={"page_title":page_title}
        return render(request, "login.html", context)

    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
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
