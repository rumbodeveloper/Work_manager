
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from TaskManager.models import Project


def index(request):
    return render(request, 'en/public/index.html')

def project_list (request):
    all_projects = Project.objects.all()
    return render(request, 'en/public/projectlist.html', {'action': "Display all projects", 'all_projects': all_projects})


def connection(request):
    return render(request, 'en/public/connection.html')