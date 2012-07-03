import base64
import unittest

from django.test.client import Client
from django.contrib.auth.models import User


class BaseAuthenticatedClient(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create_user('username', 'user@example.com', 'password')
        self.client = Client()
#        auth = '%s:%s' % (self.user.username, self.user.password)
#        auth = 'Basic %s' % base64.encodestring(auth)
#        auth = auth.strip()
#        self.extra = {
#            'HTTP_AUTHORIZATION': auth,
#        }
        self.client.login(username=self.user.username, password=self.user.password)

    def tearDown(self):
        self.user.delete()
