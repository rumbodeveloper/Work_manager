__author__ = 'Angel_Luis'

'''
Date = '22/2/15'
'''

from TaskManager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.utils import timezone

def page(request):
    #saving a new supervisor
    new_supervisor = Supervisor(name='Guido van Rossum',login='python', password='password',
                                last_connection=timezone.now(), email='python@python.com',
                                specialisation='Python')
    new_supervisor.save()
    #saving a new developer
    new_developer = Developer(name='Me', login='me',password='pass',
                              last_connection=timezone.now(), email='me@python.com',
                              supervisor=new_supervisor)
    new_developer.save()
    #saving a new task
    projecto_to_link = Project.objects.get(id=1)
    new_task = Task(title="Adding relaton",description='Exampler of adding relation and save it',
                    time_elapsed=2, importance=0, project=projecto_to_link, developer=new_developer)

    return render(request,'en/public/index.html', {'action':'Save relationship'})


def updatemodel_single_record(request):
    new_project = Project(title='Other project',description='Try to update models.',
                          client_name='People')
    new_project.save()
    task = Task.objects.get(id=1)
    task.description='New description'
    task.project= new_project
    task.save()
    return(render, 'en/public/index.html', {'action': 'Update model'})

def updatemodel_several_records(request):
    task = Project.objects.filter(client_name='Peopel').update(client_name='Nobody')
    return render(request, 'en/public/index.html', {'action':'Update for many model'})

def delete_a_record(request):
    one_task = Task.objects.get(id=1)
    one_task.delete()
    all_tasks = Task.objects.all()
    all_tasks.delete()
    return render(request, 'n/public/index.html', {'action':'Delete tasks'})

def getting_linked_records(request):
    project = Project.objects.get(id=1)
    tasks = Task.objects.filter(project=project)
    return render(request, 'en/public/index.html', {'action': 'Tasks for project', 'tasks':tasks})

def other_getting_linked_records(request):
    task = Task.objects.get(id=1)
    project = Task.project
    return render(request, 'en/public/index.html', {'action': 'Project for task', 'project': project})

