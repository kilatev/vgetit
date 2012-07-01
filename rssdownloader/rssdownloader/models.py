from django.db import models


class Podcasts(models.Model):
    rss = models.TextField()
    name = models.CharField(max_length=25)
    
    
class File(models.Model):
    file_name = models.CharField(max_length=255)
    podcast = models.ForeignKey(Podcasts)
