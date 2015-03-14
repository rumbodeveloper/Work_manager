from django.shortcuts import render
from TaskManager.models import Task
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required


@login_required
def page(request):
    task_list = Task.objects.all()
    last_task = 0

    if 'last_task' in request.session:
        last_task = Task.objects.get(id=request.session['last_task'])
        task_list = task_list.exclude(id=request.session['last_task'])
    return render(request, 'en/public/task_list.html',{'task_list':task_list,'last_task':last_task})


