from django.shortcuts import render
from TaskManager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def page(request):
    if request.POST:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            specialisation = form.cleaned_data['specialisaton']
            email = form.cleaned_data['email']
            new_user = User.objects.create_user(username=login,email=email,password=password)
            new_user.is_active = True
            new_user.last_name=name
            new_user.save()

            new_supervisor = Supervisor(user_auth = new_user, specialisation=specialisation)
            new_supervisor.save()
            return HttpResponseRedirect(reverse('public_index'))

        else:
            return render(request, 'en/public/create_supervisor.html',{'form':form})
    else:
        form = Form_supervisor()
    form = Form_supervisor()
    return render(request,'en/public/create_supervisor.html',{'form':form})

class Form_supervisor(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label="Login")
    email = forms.EmailField(label="Email")
    specialisaton = forms.CharField(label="Specialisation")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password_bis= forms.CharField(label="Password",widget=forms.PasswordInput)
    def clean(self):
        cleaned_data= super(Form_supervisor,self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get("password_bis")
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Las passwords no son identicas")
        return self.cleaned_data
