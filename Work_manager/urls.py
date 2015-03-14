from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from TaskManager.models import Project, Task, Developer
from django.views.generic import UpdateView

#extendiendo List View
from TaskManager.views.cbv.ListView import Project_list
from TaskManager.views.cbv.DetailView import Developer_detail
from TaskManager.views.cbv.UpdateView import Task_update_time
from TaskManager.views.cbv.DeleteView import Task_delete
from TaskManager.views.cbv.UpdateViewCustom import UpdateViewCustom



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
    #url(r'^projectlist$','TaskManager.views.projectlist.page',name='project_list'),
    url(r'^project-detail-(?P<pk>\d+)$','TaskManager.views.projectdetail.page', name='project_detail'),
    url(r'^create-developer$','TaskManager.views.createdeveloper.page', name='create_developer'),
    url(r'^create_supervisor$', 'TaskManager.views.createsupervisor.page', name='create_supervisor'),
    #url(r'^create_project$','TaskManager.views.createproject.page',name='create_project')

    #CBV --> vistas creadas automaticamente en CBV
    url(r'^create-project$', CreateView.as_view(model=Project, template_name='en/public/create_project.html',
                                               success_url='index'), name = 'create_project'),
    url(r'^create-task$', CreateView.as_view(model=Task, template_name='en/public/create_task.html',
                                               success_url='index'), name = 'create_task'),
    #url(r'^project_list$', ListView.as_view(model=Project, template_name='en/public/project_list.html'),
        #name='project_list'), # entre comillas para explorar un resultado de sobreescribir CBV'''
    url(r'^project_list$', Project_list.as_view(model=Project, template_name='en/public/project_list.html'),
        name='project_list'),
    url(r'^developer_list$', ListView.as_view(model=Developer, template_name='en/public/developer_list.html'),
        name='developer_list'),
    #url(r'task_detail(?P<pk>\d+)$', DetailView.as_view(model=Task, template_name='en/public/task_detail.html'),
        #name='task_detail'), --> esta la url antigua, sustitudia por la del capitulo 9: using sesions.
    url(r'^developer_detail(?P<pk>\d+)$', Developer_detail.as_view(),name='developer_detail'),
    #ojo, en la siguiente linea success_url es directamente la url, no el name de la url
    #url(r'^update_task(?P<pk>\d+)$', UpdateView.as_view(model=Task, template_name="en/public/update_task.html",
                                                        #success_url='index'),
                                                        #name='update_task'),
        #TODO No se como pasar el parametro pk para que la vista lo tenga en cuenta.
    url(r'^update_task_time(?P<pk>\d+)$', Task_update_time.as_view(),
        name='update_task_time'),
    url(r'^task_delete_(?P<pk>\d+)$',Task_delete.as_view(),name='task_delete'),
    url(r'^update_task_(?P<pk>\d+)$', UpdateViewCustom.as_view(model=Task,url_name='update_task',
                                                              success_url='public_index'),
                                                            name='update_task'),
    url(r'^task_detail_(?P<pk>\d+)$','TaskManager.views.task_detail.page',name='task_detail'),
    url(r'^task_list$', 'TaskManager.views.task_list.page', name='task_list'),
    url(r'^connections$','TaskManager.views.connection.page',name="public_connection"),
    url(r'^logout$','TaskManager.views.logout.page',name='public_logout'),
    url(r'^task_delete_ajax$', 'TaskManager.views.ajax.task_delete_ajax.page', name="task_delete_ajax"),
)
