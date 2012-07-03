from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rssdownloader.models import Podcasts


class TestDownloadFeedItem(unittest.TestCase):

    def setUp(self):
        super(TestDownloadFeedItem, self).setUp()

        self.username = 'test_user'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'test_user@example.com', self.password)
        self.client = Client()
        Podcasts.objects.create(rss='http://feeds.feedburner.com/NGCast', name='ngcast')
        

    def testDownloadItem(self):
        url = reverse('downloader')
        self.assertTrue(self.client.get(url))

