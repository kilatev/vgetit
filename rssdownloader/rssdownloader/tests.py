from django.utils import unittest
from django.test.client import Client


class TestDownloadFeedItem(unittest.TestCase):

    def setUp(self):
        super(TestDownloadFeedItem, self).setUp()

        self.username = 'test_user'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'test_user@example.com', self.password)

    def testDownloadItem(self):
        self.assertValidJSONResponse(self.api_client.get('/api/v1/download_files/', format='json', authentication=self.get_credentials()))

