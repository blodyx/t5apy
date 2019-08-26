from t5apy import request_api_key
from t5apy import request_map_data
from t5apy.fixtures import BASE_URL

import unittest
from unittest.mock import patch


class Testt5apy(unittest.TestCase):

    @patch('t5apy.http')
    @patch('t5apy.json')
    def testing_request_api_key(self, mock_json, mock_http):
        mock_json.loads.return_value = {'response': 'mocked'}
        r = request_api_key(
            email='test@email.com',
            site_name='unittest',
            site_url='https://example.com',
            public='false',
            gameworld='test',
        )

        mock_http.request.assert_called_with(
            method='GET',
            url=BASE_URL % 'test',
            params={
                'action': 'requestApiKey',
                'email': 'test@email.com',
                'siteName': 'unittest',
                'siteUrl': 'https://example.com',
                'public': 'false',
            },
        )
        mock_json.loads.assert_called_with(mock_http.request())
        self.assertEqual(r, 'mocked')

    @patch('t5apy.http')
    @patch('t5apy.json')
    def testing_request_map_data(self, mock_json, mock_http):
        mock_json.loads.return_value = {'response': 'mocked'}
        r = request_map_data(
            private_api_key='private api key',
            gameworld='test',
        )

        mock_http.request.assert_called_with(
            method='GET',
            url=BASE_URL % 'test',
            params={
                'action': 'getMapData',
                'privateApiKey': 'private api key',
            },
        )
        mock_json.loads.assert_called_with(mock_http.request())
        self.assertEqual(r, 'mocked')


if __name__ == '__main__':
    unittest.run()
