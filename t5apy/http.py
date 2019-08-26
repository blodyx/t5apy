""" Module `http.py` is for `t5apy` make HTTP request to Travian 5 API
end points.
"""

import urllib.request
import urllib.parse

from . import __version__
from . import __name__


def request(method, url, params={}):
    """ Make HTTP request to URL.

    Parameters:
        method: `string` HTTP method.
        url: `string` URL.
        params: `dict` passing data to URL's query strings.
    """

    headers = {
        'User-Agent': 'Python-%s/%s' % (__name__, __version__),
    }

    if params:
        url = '?'.join([url, urllib.parse.urlencode(params, safe='@ : /')])

    req = urllib.request.Request(
        url=url,
        method=method,
        headers=headers,
    )

    with urllib.request.urlopen(req, timeout=60.0) as r:
        return r.read()
