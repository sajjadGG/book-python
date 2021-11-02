Comprehension Nested
====================


Syntax
------
>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten']}
>>>
>>> result = {}
>>> for i, titles in DATA.items():
...     for title in titles:
...         result[title] = str(i)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': '6',
 'Prof-school': '6',
 'Masters': '5',
 'Bachelor': '5',
 'Engineer': '5',
 'HS-grad': '4',
 'Junior High': '3',
 'Primary School': '2',
 'Kindergarten': '1'}
>>>
>>> print(i)
1
>>>
>>> print(title)
Kindergarten
>>>
>>> print(titles)
['Kindergarten']

>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten']}
>>>
>>> result = {title: str(i)
...           for i, titles in DATA.items()
...           for title in titles}
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': '6',
 'Prof-school': '6',
 'Masters': '5',
 'Bachelor': '5',
 'Engineer': '5',
 'HS-grad': '4',
 'Junior High': '3',
 'Primary School': '2',
 'Kindergarten': '1'}
>>>
>>> # doctest: +SKIP
... print(i)
Traceback (most recent call last):
NameError: name 'i' is not defined
>>>
>>> # doctest: +SKIP
... print(title)
Traceback (most recent call last):
NameError: name 'title' is not defined
>>>
>>> # doctest: +SKIP
... print(titles)
Traceback (most recent call last):
NameError: name 'titles' is not defined


Code Readability
----------------
>>> DATA = [{'a':1, 'b':2, 'c': 3},
...         {'a':1, 'b':2, 'c': 3},
...         {'a':1, 'b':2, 'c': 3}]
>>>
>>> result = [value
...           for row in DATA
...             for key, value in row.items()]
>>>
>>> result = [value
...           for row in DATA
...           for key, value in row.items()]
>>>

>>> # doctest: +SKIP
... result = [astronaut | dict(addresses)
...           for astronaut in json.loads(DATA)
...             for i, address in enumerate(astronaut.pop('addresses'), start=1)
...                 if (columns := [f'{key}{i}' for key in address.keys()])
...                     and (addresses := zip(columns, address.values()))]
>>>
>>> # doctest: +SKIP
... result = [astronaut | dict(addresses)
...           for astronaut in json.loads(DATA)
...           for i, address in enumerate(astronaut.pop('addresses'), start=1)
...           if (columns := [f'{key}{i}' for key in address.keys()])
...           and (addresses := zip(columns, address.values()))]


Assignments
-----------
.. literalinclude:: assignments/comprehension_nested_a.py
    :caption: :download:`Solution <assignments/comprehension_nested_a.py>`
    :end-before: # Solution
