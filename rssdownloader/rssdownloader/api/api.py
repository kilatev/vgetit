from piston.handler import BaseHandler
from rssdownloader.models import Mp3File


class Mp3FileHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Mp3File
    def read(self, request):
        return Mp3File.objects.download()
