
# Create your views here.
from django.shortcuts import render

from TaskManager.models import Project




def page(request,pk):
    project = Project.objects.get(id=pk)
    return render(request, 'en/public/project_detail.html', {'project':project})

