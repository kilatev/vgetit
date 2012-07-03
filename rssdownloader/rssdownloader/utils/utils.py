import base64
import unittest
from django.test.client import Client

class BaseAuthenticatedClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        auth = '%s:%s' % ('username', 'password')
        auth = 'Basic %s' % base64.encodestring(auth)
        auth = auth.strip()
        self.extra = {
            'HTTP_AUTHORIZATION': auth,
        }
