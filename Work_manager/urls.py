from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^Work_manager/', include('Work_manager.foo.urls')),
    url(r'^$','TaskManager.views.index'),
    url(r'^index$','TaskManager.index.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
