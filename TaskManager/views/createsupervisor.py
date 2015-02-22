from django.shortcuts import render
from TaskManager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class Form_supervisor(forms.ModelForm):
    class Meta:
        model = Supervisor
        exclude = ('date_created', 'last_connection',)



def page(request):
    if len(request.POST)>0:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('public_index'))
        else:
            return render(request, 'en/public/create_supervisor.html',{'form':form})
    else:
        form = Form_supervisor()
        return render(request, 'en/public/create_supervisor.html',{'form':form})





