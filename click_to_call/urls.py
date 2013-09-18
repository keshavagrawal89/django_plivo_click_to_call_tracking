from django.conf.urls import patterns, include, url
import os.path
from django.views.generic import TemplateView
from clicktocall.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
	(r'^$', main_page),
	(r'^send_call/$', send_call),
	(r'^dialagent/$', dialagent),
	(r'^hangup_lead/$', hangup_lead),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    # Examples:
    # url(r'^$', 'click_to_call.views.home', name='home'),
    # url(r'^click_to_call/', include('click_to_call.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
