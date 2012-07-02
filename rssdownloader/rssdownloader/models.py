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
        file = Mp3File()
        for podcast in podcasts:
            feed = feedparser.parse(podcast.rss)
            for item in feed['items']:
                filename = os.path.join(settings.MP3_STORAGE, item.title)
                if not Mp3File.objects.filter(pub_date=item['date'], podcast=podcast):
                    self._download(item.link, filename)
                    
                    file.file_name = item.title
                    file.podcast = podcast
                    file.pub_date = item['date']
                    file.save()

        return file

    def _download(self, url, filename):
        u = urllib2.urlopen(url)
        h = u.info()
        fp = open(filename, 'wb')

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
    pub_date = models.DateField()
    objects = FileManager()
