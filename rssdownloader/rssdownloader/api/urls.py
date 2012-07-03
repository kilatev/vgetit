from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from rssdownloader.api import Mp3FileHandler, PodcastsHandler, PodcastsListHandler, PodcastsCreateHandler


auth = HttpBasicAuthentication(realm="rssdownloader")
ad = { 'authentication': auth }

mp3file_handler = Resource(Mp3FileHandler, **ad)
podcasts_handler = Resource(PodcastsHandler, **ad)
podcasts_list_handler = Resource(PodcastsListHandler, **ad)
podcasts_create_handler = Resource(PodcastsCreateHandler, **ad)

urlpatterns = patterns('',
    url(r'^download/$', mp3file_handler, { 'emitter_format': 'json' }, name='downloader'),
    url(r'^podcasts$', podcasts_create_handler, { 'emitter_format': 'json' }, name='podcasts_create'),
    url(r'^podcasts/$', podcasts_list_handler, { 'emitter_format': 'json' }, name='list_podcasts'),
    url(r'^podcasts/(?P<name>[^/]+)/$', podcasts_handler, { 'emitter_format': 'json' }, name='podcasts'),

)