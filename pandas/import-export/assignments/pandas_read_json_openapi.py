"""
* Assignment: Pandas Read JSON OpenAPI
* Filename: pandas_read_json_openapi.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` as `result: pd.DataFrame`
    3. Use `requests` library
    4. Print `result`

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    3. Użyj biblioteki `requests`
    4. Wypisz `result`

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> list(result.index)
    ['put', 'post', 'get', 'delete']
    >>> list(result.columns)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""


# Given
import pandas as pd
import requests

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/openapi.json'


# Solution
data = requests.get(DATA).json()
result = pd.DataFrame(data['paths'])
