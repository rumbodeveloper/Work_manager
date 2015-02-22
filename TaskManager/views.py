
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from TaskManager.models import Project,  Supervisor


def index(request):
    return render(request, 'en/public/index.html')

def project_list (request):
    all_projects = Project.objects.all()
    return render(request, 'en/public/projectlist.html', {'action': "Display all projects", 'all_projects': all_projects})


def connection(request):
    return render(request, 'en/public/connection.html')

def project_detail(request,pk):
    project = Project.objects.get(id=pk)
    return render(request, 'en/public/project_detail.html', {'project':project})

def create_developer(request):
    supervisors_list = Supervisor.objects.all()
    return render(request, 'en/public/create_developer.html',{'supervisors_list': supervisors_list})