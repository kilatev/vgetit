from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from models import Podcasts, Mp3File

class PodcastsResource(ModelResource):
    class Meta:
        queryset = Podcasts.objects.all()
        resource_name = 'podcasts'
        #authorization= Authorization()


class FileResource(ModelResource):
    class Meta:
        queryset = Mp3File.objects.download()
        resource_name = 'download_files'
