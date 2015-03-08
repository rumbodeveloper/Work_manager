from django.shortcuts import render
from TaskManager.models import  Task
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def page(request,pk):
    check_task = Task.objects.filter(id=pk)



    try:
        task=check_task.get()
    except (Task.DoesNotExist, Task.MultipleObjectsReturned):
        return HttpResponseRedirect(reverse('public_index'))


    request.session['last_task']=task.id

    return render(request, 'en/public/task_detail.html',{'object':task})

