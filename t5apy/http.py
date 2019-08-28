""" Module `http.py` is for `t5apy` make HTTP request to Travian 5 API
end points.
"""

try:
    import urllib.request as urllib_request
    import urllib.parse as urllib_parse
except ImportError:
    import urllib2 as urllib_request
    from . import urllib_parse

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
        url = '?'.join([url, urllib_parse.urlencode(params, safe='@ : /')])

    req = urllib_request.Request(
        url=url,
        method=method,
        headers=headers,
    )

    with urllib_request.urlopen(req, timeout=60.0) as r:
        return r.read()
