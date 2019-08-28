import unittest
import collections
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from t5apy import __name__
from t5apy import __version__
from t5apy.http import request


class TestHTTP(unittest.TestCase):

    def setUp(self):
        self.headers = {
            'User-Agent': 'Python-%s/%s' % (__name__, __version__),
        }
        self.url = 'https://httpbin.org/get'

    @patch('t5apy.http.urllib_request')
    def test_request(self, mock_request):
        mock_request.urlopen().__enter__().read.return_value = 'mocked'

        r = request('GET', self.url)

        mock_request.Request.assert_called_with(
            url=self.url,
            method='GET',
            headers=self.headers,
        )
        mock_request.urlopen.assert_called_with(
            mock_request.Request(),
            timeout=60.0,
        )
        self.assertEqual(r, 'mocked')

        # testing again with params
        params = collections.OrderedDict([('a', 'a'), ('b', 'b'), ('c', 'c')])
        r = request('GET', self.url, params)

        mock_request.Request.assert_called_with(
            url=self.url + '?a=a&b=b&c=c',
            method='GET',
            headers=self.headers
        )
        mock_request.urlopen.assert_called_with(
            mock_request.Request(),
            timeout=60.0,
        )
        self.assertEqual(r, 'mocked')


if __name__ == '__main__':
    unittest.run()
