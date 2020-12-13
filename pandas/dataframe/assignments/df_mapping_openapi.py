"""
* Assignment: Pandas Read JSON OpenAPI
* Filename: :download:`assignments/pandas_read_json_openapi.py`
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` as `result: pd.DataFrame`
    3. Use `requests` library
    4. Transpose data
    5. If cell is a `dict`, then extract value for `summary`
    6. If cell is empty, leave `pd.NA`

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    3. Użyj biblioteki `requests`
    4. Transponuj dane
    5. Jeżeli komórka jest `dict`, to wyciągnij wartość dla `summary`
    6. Jeżeli komórka jest pusta, pozostaw `pd.NA`

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> list(result.columns)
    ['put', 'post', 'get', 'delete']
    >>> list(result.index)  # doctest: +NORMALIZE_WHITESPACE
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
result = (pd.DataFrame(data['paths'])
            .transpose()
            .applymap(lambda x: x['summary'] if type(x) == dict else pd.NA))
