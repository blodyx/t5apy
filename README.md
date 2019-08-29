# t5apy

Request public map data from Travian 5 API more convenient with `t5apy`.  
This [[official thread](https://forum.kingdoms.com/index.php?thread/4099-api-for-external-tools/)] explain on how to use Travian 5 API.

[![Build Status](https://travis-ci.org/didadadida93/t5apy.svg?branch=master)](https://travis-ci.org/didadadida93/t5apy) [![codecov](https://codecov.io/gh/didadadida93/t5apy/branch/master/graph/badge.svg)](https://codecov.io/gh/didadadida93/t5apy) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

# Installation

> it's recommended to use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/).

1. git clone this repo  
`(venv)$ git clone https://github.com/didadadida93/t5apy.git`
2. change directory to t5apy.  
`(venv)$ cd t5apy`
3. install it  
`(venv)$ pip install .`

# Usage

Based on [[official thread](https://forum.kingdoms.com/index.php?thread/4099-api-for-external-tools/)] first we need API key.  
After that we can request public map data.
```python
>>> import t5apy
>>>
>>> api_key = t5apy.request_api_key(
...     email='your@email.com',
...     site_name='your-tools',
...     site_url='https://example.com',
...     public='false',
...     gameworld='com1'
... )
>>>
>>> # once we get api key, we can request public map data
... map_data = t5apy.request_map_data(
...     private_api_key=api_key['privateApiKey'],
...     gameworld='com1'
... )
>>> map_data.keys()
dict_keys(['gameworld', 'players', 'kingdoms', 'map'])
>>>
```
