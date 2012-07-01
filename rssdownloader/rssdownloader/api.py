from tastypie.resources import ModelResource
from models import Podcasts

class PodcastsResource(ModelResource):
    class Meta:
        queryset = Podcasts.objects.all()
        resource_name = 'podcasts'
        authorization= Authorization()