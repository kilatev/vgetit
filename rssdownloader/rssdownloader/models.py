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
        for podcast in podcasts:
            feed = feedparser.parse(podcast.rss)
            for item in feed['items']:
                filename = os.path.join(settings.MP3_STORAGE, item.title)
                self._download(item.link, filename)

        pass

    def _download(self, url, filename):
        u = urllib2.urlopen(remote)
        h = u.info()
        totalSize = int(h["Content-Length"])

        print "Downloading %s bytes..." % totalSize,
        fp = open(local, 'wb')

        blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
        count = 0
        while True:
            chunk = u.read(blockSize)
            if not chunk: break
            fp.write(chunk)
            count += 1
            if totalSize > 0:
                percent = int(count * blockSize * 100 / totalSize)
                if percent > 100: percent = 100
                print "%2d%%" % percent,
                if percent < 100:
                    print "\b\b\b\b\b", # Erase "NN% "
                else:
                    print "Done."

        fp.flush()
        fp.close()



class File(models.Model):
    file_name = models.CharField(max_length=255)
    podcast = models.ForeignKey(Podcasts)
    objects = FileManager()
