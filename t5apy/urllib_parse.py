""" Module `urllib_parse.py` only imported when `t5apy` being used on
python 2. If this module is imported with python 3, it will raise
`AttributeError`.
"""

import urllib


def urlencode(params, safe=''):
    """ `urlencode` try to substitute missing `urllib.parse.urlencode`
    from python 3 if `t5apy` running on python 2.

    ---

    Parameters:
        params: `dict` data that want to be encoded into URL query
                string.
        safe: `string` string that didn't want to be encoded.

    return: `string`

    ---

    Usage:
        >>> urlencode({'a':'a', 'b':'b', 'c':'c'})
        'a=a&b=b&c=c'
    """
    
    return '&'.join(
        [
            '='.join(
                [urllib.quote_plus(k, safe), urllib.quote_plus(v, safe)]
            )
            for k, v in params.items()
        ]
    )
