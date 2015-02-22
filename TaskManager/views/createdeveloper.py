
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from TaskManager.models import  Developer, Supervisor
from django import forms

#esta seria la funcion real, utilizando la facilidad de formas de django

class Form_inscription(forms.Form):
    name = forms.CharField(label='Name',max_length=30)
    login = forms.CharField(label='Login',max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label='Supervisor', queryset=Supervisor.objects.all())


def page(request):
    if request.POST:
        form = Form_inscription(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']
            new_developer = Developer(name= name, login=login,
                                      password=password,email='', supervisor=supervisor)
            new_developer.save()
            return HttpResponse('Desarrollador agregado')
        else:
            return render(request, 'en/public/create_developer.html', {'form':form})
    else:
        form=Form_inscription()
        return render(request, 'en/public/create_developer.html', {'form':form})






#funcion inicial, solo muestra un combo
'''def page(request):
    supervisors_list = Supervisor.objects.all()
    return render(request, 'en/public/create_developer.html',{'supervisors_list': supervisors_list})'''
#esta seria la funcion tradicional usando codigo html
'''def page(request):
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
        return render(request, 'en/public/create_developer.html',{'supervisors_list': supervisors_list})'''
