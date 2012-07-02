from piston.handler import BaseHandler
from .models import Mp3File

class Mp3FileHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Mp3File
    def read(self, request):
        Mp3File.objects.download()  
