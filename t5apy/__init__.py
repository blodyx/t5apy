__name__ = 't5apy'
__version__ = '0.0.1'
__author__ = 'didadadida93'
__author_email__ = 'didadadida93@gmail.com'
__description__ = 'Request public map data from Travian 5 API easily'
__license__ = 'MIT'


import json

from . import http
from .fixtures import BASE_URL


def request_api_key(email, site_name, site_url, public, gameworld):
    """ Request API key to Travian 5 API endpoints.
    Based on official thread, it need to get API key first before
    request public map data from Travian 5 API endpoints.

    ---

    Parameters:
        email: `string` valid email.
        site_name: `string` name of the tool.
        site_url: `string` url of the tool - needs to be a valid url.
        public: `string` it is either 'true' or 'false'.
        gameworld: `string` which gameworld that you want to request
                   the api key.

    return: `dict`

    ---

    Usage:
        >>> import t5apy
        >>> api_key = t5apy.request_api_key(
        ...     email='your@email.com',
        ...     site_name='your-tools',
        ...     site_url='https://example.com',
        ...     public='false',
        ...     gameworld='com1',
        ... )
        >>> api_key
        {'privateApiKey': '...', 'publicSiteKey': '...'}
    """

    params = {
        'action': 'requestApiKey',
        'email': email,
        'siteName': site_name,
        'siteUrl': site_url,
        'public': public,
    }

    raw_response = http.request(
                       method='GET',
                       url=BASE_URL % gameworld,
                       params=params,
                   )

    return json.loads(raw_response)['response']


def request_map_data(private_api_key, gameworld):
    """ Request public map data from Travian 5 API endpoints.
    Before use this function, make sure you have private api key from
    Travian 5. You can use :func:`request_api_key` for get the private
    api key.

    ---

    Parameters:
        private_api_key: `string` private api key from Travian 5.
                         This private api key should be related
                         to gameworld.
        gameworld: `string` which gameworld that you want to request
                   public map data. This gameworld should be related
                   with private api key.

    return: `dict`

    ---

    Usage:
        >>> # using api_key from t5apy.request_api_key() above
        ... r = t5apy.request_map_data(
        ...     private_api_key=api_key['privateApiKey'],
        ...     gameworld='com1',
        ... )
        >>> r.keys()
        dict_keys(['gameworld', 'players', 'kingdoms', 'map'])
    """

    params = {
        'action': 'getMapData',
        'privateApiKey': private_api_key,
    }

    raw_response = http.request(
                       method='GET',
                       url=BASE_URL % gameworld,
                       params=params,
                   )

    return json.loads(raw_response)['response']
