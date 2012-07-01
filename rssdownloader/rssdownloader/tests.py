import unitests
from tastypie.test import ResourceTestCase


class DownloadFeedItemTest(ResourceTestCase):

    def setUp(self):
        super(EntryResourceTest, self).setUp()

        # Create a user.
        self.username = 'test_user'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'test_user@example.com', self.password)

    def testDownloadItem(self):
        self.assertValidJSONResponse(self.api_client.get('/api/v1/download_files/', format='json', authentication=self.get_credentials()))

