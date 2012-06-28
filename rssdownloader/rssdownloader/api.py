from tastypie.resources import ModelResource
from myapp.models import Entry

class PodcastsResource(ModelResource):
    class Meta:
        queryset = Podcasts.objects.all()
        resource_name = 'podcasts'