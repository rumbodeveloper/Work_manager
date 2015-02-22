
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from TaskManager.models import  Developer, Supervisor



'''def page(request):
    supervisors_list = Supervisor.objects.all()
    return render(request, 'en/public/create_developer.html',{'supervisors_list': supervisors_list})'''

def page(request):
    error = False
    
    if request.POST:
        if 'name' in request.POST:
            name = request.POST.get('name','')
        else:
            error=True

        if 'login' in request.POST:
            login = request.POST.get('login','')
        else:
            error=True
            
        if 'password' in request.POST:
            password = request.POST.get('password','')
        else:
            error=True
            
        if 'supervisor' in request.POST:
            supervisor_id = request.POST.get('supervisor','')
        else:
            error=True
            
        if not error:
            supervisor = Supervisor.objects.get(id=supervisor_id)
            new_dev = Developer(name=name, login=login, password=password, supervisor=supervisor)
            new_dev.save()
            return HttpResponse('Desarrollador agregado')
        else:
            return HttpResponse('Ha habido algun error')
    else:
        supervisors_list = Supervisor.objects.all()
        return render(request, 'en/public/create_developer.html',{'supervisors_list': supervisors_list})
