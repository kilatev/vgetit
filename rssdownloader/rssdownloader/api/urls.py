from django.conf.urls.defaults import *

from piston.resource import Resource

from rssdownloader.api import Mp3FileHandler, PodcastsHandler, PodcastsListHandler, PodcastsCreateHandler


mp3file_handler = Resource(Mp3FileHandler)
podcasts_handler = Resource(PodcastsHandler)
podcasts_list_handler = Resource(PodcastsListHandler)
podcasts_create_handler = Resource(PodcastsCreateHandler)

urlpatterns = patterns('',
    url(r'^download/$', mp3file_handler, { 'emitter_format': 'json' }, name='downloader'),
    url(r'^podcasts$', podcasts_create_handler, { 'emitter_format': 'json' }, name='podcasts_create'),
    url(r'^podcasts/$', podcasts_list_handler, { 'emitter_format': 'json' }, name='list_podcasts'),
    url(r'^podcasts/(?P<name>[^/]+)/$', podcasts_handler, { 'emitter_format': 'json' }, name='podcasts'),

)