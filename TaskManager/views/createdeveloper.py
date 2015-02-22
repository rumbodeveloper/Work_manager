
# Create your views here.
from django.shortcuts import render

from TaskManager.models import   Supervisor



def page(request):
    supervisors_list = Supervisor.objects.all()
    return render(request, 'en/public/create_developer.html',{'supervisors_list': supervisors_list})