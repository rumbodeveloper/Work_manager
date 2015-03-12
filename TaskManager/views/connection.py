
# Create your views here.
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login


def page(request):
    if request.POST:
        form = Form_connection(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
        else:
            return render(request,'en/public/connection.html',{'form':form})
    else:
        form = Form_connection()
    return render(request,'en/public/connection.html',{'form':form})



class Form_connection(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(Form_connection,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not  authenticate(username=username, password=password):
            raise forms.ValidationError("Error en el login o en la password")
        return self.cleaned_data
