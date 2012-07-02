from django.conf.urls.defaults import *

from piston.resource import Resource

from .api import Mp3FileHandler


mp3file_handler = Mp3FileHandler()


urlpatterns = patterns('',
    url(r'^download/', mp3file_handler, name='downloader'),
)