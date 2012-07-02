from django.utils import unittest
from django.test.client import Client

from django.contrib.auth.models import User


class TestDownloadFeedItem(unittest.TestCase):

    def setUp(self):
        super(TestDownloadFeedItem, self).setUp()

        self.username = 'test_user'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'test_user@example.com', self.password)
        self.client = Client()

    def testDownloadItem(self):
        self.assertTrue(self.client.get('/api/v1/download_files/'))

