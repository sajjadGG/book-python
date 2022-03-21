FuncProg First-class Functions
==============================
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...
* Function can be returned
* Function can be user as a parameter


Assigning Functions
-------------------
* Function can be assigned to variable

>>> def say_hello():
...     return 'hello world'
>>>
>>>
>>> result = say_hello
>>> result()
'hello world'


Storing Functions
-----------------
* Function can be stored in data structures such as hash tables, lists, ...

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> operations = (cube, square)

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> operations = {
...     'cube': cube,
...     'square': square,
...     'root': lambda x: x ** (1/2)
... }


Returning Functions
-------------------
* Function can be returned

>>> def lower():
...     return 'Hello world'
>>>
>>>
>>> def higher():
...     return lower
>>>
>>>
>>> result = higher()     # <function lower()>
>>> result()              # 'Hello world'
'Hello world'


Parameter Functions
-------------------
* Function can be user as a parameter

>>> def http_request(url, on_success, on_error):
...     try:
...         result = ...
...     except Exception as error:
...         return on_error(error)
...     else:
...         return on_success(result)
>>>
>>>
>>> http_request(
...     url = 'https://python.astrotech.io',
...     on_success = lambda result: print(result),
...     on_error = lambda error: print(error))
Ellipsis


Use Case - 0x01
---------------
>>> def map(func, data):
...     ...

>>> def filter(func, data):
...     ...

>>> def reduce(func, data):
...     ...


Use Case - 0x02
---------------
>>> # doctest: +SKIP
... import pandas as pd
...
...
... DATA = 'https://python.astrotech.io/_static/phones-pl.csv'
...
... result = (
...     pd
...     .read_csv(DATA, parse_dates=['datetime'])
...     .set_index('datetime', drop=True)
...     .drop(columns=['id'])
...     .loc['2000-01-01':'2000-03-01']
...     .query('item == "sms"')
...     .groupby(['period','item'])
...     .agg(
...         duration_count = ('duration', 'count'),
...         duration_sum = ('duration', 'sum'),
...         duration_median = ('duration', 'median'),
...         duration_mean = ('duration', 'mean'),
...         duration_std = ('duration', 'std'),
...         duration_var = ('duration', 'var'),
...         value = ('duration', lambda column: column.mean().astype(int))
...     )
... )
