
# Create your views here.
from django.shortcuts import render
from TaskManager.models import Project



def page(request):
    all_projects = Project.objects.all()
    return render(request, 'en/public/projectlist.html', {'action': "Display all projects", 'all_projects': all_projects})


