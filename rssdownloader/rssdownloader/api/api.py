from piston.handler import BaseHandler
from rssdownloader.models import Mp3File
from rssdownloader.models import Podcasts
from piston.utils import rc


class Mp3FileHandler(BaseHandler):

  allowed_methods = ('GET',)

  def read(self, request):
      return str(Mp3File.objects.download())


class PodcastsHandler(BaseHandler):

    allowed_methods = ('GET', 'PUT', 'DELETE',)

    def read(self, request, name):
        return Podcasts.objects.get(name=name)

    def delete(self, request, name):
        podcast = Podcasts.objects.get(name=name)
        podcast.delete()
        return rc.DELETED

    def update(self, request, name):
        print "aaa"
        data = request.GET
        print data
        podcast = Podcasts.objects.get(name=name)
        podcast.rss = data['rss']
        podcast.save()
        return rc.ALL_OK


class PodcastsListHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Podcasts.objects.all()


class PodcastsCreateHandler(BaseHandler):
    model = Podcasts 
    alowed_methods = ('POST',)
    
    def create(self, request):
        data = request.GET
        podcast = Podcasts.objects.create(rss=data['rss'], name=data['name'])
        return rc.CREATED
