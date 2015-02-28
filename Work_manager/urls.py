from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import CreateView
from TaskManager.models import Project, Task

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^Work_manager/', include('Work_manager.foo.urls')),
    url(r'^$','TaskManager.views.index.page',name='public_index'),
    url(r'^index$','TaskManager.views.index.page',name='public_index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^connection$','TaskManager.views.connection.page',name='public_connection'),
    url(r'^projectlist$','TaskManager.views.projectlist.page',name='project_list'),
    url(r'^project-detail-(?P<pk>\d+)$','TaskManager.views.projectdetail.page', name='project_detail'),
    url(r'^create-developer$','TaskManager.views.createdeveloper.page', name='create_developer'),
    url(r'^create_supervisor$', 'TaskManager.views.createsupervisor.page', name='create_supervisor'),
    #url(r'^create_project$','TaskManager.views.createproject.page',name='create_project')
    url(r'create-project$', CreateView.as_view(model=Project, template_name='en/public/create_project.html',
                                               success_url='index'), name = 'create_project'),
    url(r'create-task$', CreateView.as_view(model=Task, template_name='en/public/create_task.html',
                                               success_url='index'), name = 'create_task')
)
