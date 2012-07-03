from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse

from rssdownloader.models import Podcasts
from rssdownloader.utils import BaseAuthenticatedClient


class TestDownloadFeedItem(BaseAuthenticatedClient):

    def testDownloadItem(self):
        url = reverse('downloader')
        self.assertTrue(self.client.get(url))
    
    
class TestPodcastsRest(BaseAuthenticatedClient): 
 
    def testCreatePodcast(self):
        url = reverse('podcasts_create')
        data= dict(name='test', rss='rssurl')
        self.assertTrue(self.client.put(url, **data))
        
    def testListPodcast(self):
        url = reverse('podcasts_create')
        data = {}
        data['name']='test0'
        data['rss']='rssurl0'
        
        resp = self.client.put(url, data, **self.extra)
        data['name']='test2'
        data['rss']='rssurl2'
        self.client.put(url, data, **self.extra)
         
        url = reverse('list_podcasts')
        data= dict(name='test', rss='rssurl')
        res = self.client.get(url, **self.extra)
        self.assertTrue(self.client.get(url))

