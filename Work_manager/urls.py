from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^Work_manager/', include('Work_manager.foo.urls')),
    url(r'^$','TaskManager.views.index',name='public_index'),
    url(r'^index$','TaskManager.views.index',name='public_index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^connection$','TaskManager.views.connection',name='public_connection'),
    url(r'^projectlist$','TaskManager.views.project_list',name='project_list'),
    url(r'^project-detail-(?P<pk>\d+)$','TaskManager.views.project_detail', name='project_detail'),
    url(r'^create-developer$','TaskManager.views.create_developer', name='create_developer'),
)
