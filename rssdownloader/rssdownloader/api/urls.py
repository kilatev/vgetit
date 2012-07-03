from django.conf.urls.defaults import *

from piston.resource import Resource

from rssdownloader.api import Mp3FileHandler


mp3file_handler = Resource(Mp3FileHandler)


urlpatterns = patterns('',
    url(r'^download$', mp3file_handler, { 'emitter_format': 'json' }, name='downloader'),
)