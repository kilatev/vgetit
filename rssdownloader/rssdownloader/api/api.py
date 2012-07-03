from piston.handler import BaseHandler
from rssdownloader.models import Mp3File


class Mp3FileHandler(BaseHandler):
    
    allowed_methods = ('GET',)
    
    def read(self, request):
        res = str(Mp3File.objects.download())
        print "Result ", res
        return res
