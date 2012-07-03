import os
import feedparser
import urllib2

from django.db import models
from django.conf import settings


class Podcasts(models.Model):
    rss = models.TextField()
    name = models.CharField(max_length=25)


class FileManager(models.Manager):
    
    def download(self):
        podcasts = Podcasts.objects.all()
        file_list = []
        mfile = ""
        for podcast in podcasts:
            feed = feedparser.parse(podcast.rss)
            for item in feed['items']:
                mp3url = item['links'][1]['href']
                name= mp3url.split('/')[-1]
                filename = os.path.join(settings.MP3_STORAGE, name)
                mp3files = Mp3File.objects.filter(pub_date=item['published'], podcast=podcast)
                if not mp3files:
                    self._download(mp3url, filename)
                    mfile = Mp3File.objects.create(file_name=filename, podcast=podcast, pub_date=item['published'])
                    file_list.append(name)
                    
        return file_list

    def _download(self, url, filename):
        u = urllib2.urlopen(url)
        h = u.info()
        try:
            fp = open(os.path.abspath(filename), 'wb')
        except:
            self.logger.info("Failed to Download file %s" % filename)
        block_size = 8192
        count = 0

        while True:
            chunk = u.read(block_size)
            if not chunk: break
            fp.write(chunk)
        fp.flush()
        fp.close()


class Mp3File(models.Model):
    file_name = models.CharField(max_length=255)
    podcast = models.ForeignKey(Podcasts)
    pub_date = models.CharField(max_length=100)
    objects = FileManager()
