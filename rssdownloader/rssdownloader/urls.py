from django.conf.urls import patterns, include, url
from django.contrib import admin

from .api import PodcastsResource


admin.autodiscover()

podcasts_resource = PodcastsResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rssdownloader.views.home', name='home'),
     #Surl(r'^rssdownloader/', include('rssdownloader.foo.urls')),
     (r'^api/', include(podcasts_resource.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
