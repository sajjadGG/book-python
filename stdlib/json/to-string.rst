JSON To String
==============


Mapping
-------
* ``json.dumps(DATA: dict) -> str``
* ``json.loads(DATA: str) -> dict``

Serialize mapping to JSON:

>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney'}
>>>
>>>
>>> result = json.dumps(DATA)
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney"}

Deserialize JSON to mapping:

>>> import json
>>>
>>>
>>> DATA = """
...     {"firstname": "Mark",
...      "lastname": "Watney"}"""
>>>
>>>
>>> result = json.loads(DATA)
>>>
>>> print(result)
{'firstname': 'Mark', 'lastname': 'Watney'}


List of Mappings
----------------
* ``json.dumps(data: Sequence[dict]) -> str``
* ``json.loads(data: str) -> list[dict]``

Serialize list of mappings to JSON:

>>> import json
>>>
>>>
>>> DATA = [{'firstname': 'Melissa', 'lastname': 'Lewis'},
...         {'firstname': 'Rick', 'lastname': 'Martinez'},
...         {'firstname': 'Mark', 'lastname': 'Watney'}]
>>>
>>>
>>> result = json.dumps(DATA)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{"firstname": "Melissa", "lastname": "Lewis"},
 {"firstname": "Rick", "lastname": "Martinez"},
 {"firstname": "Mark", "lastname": "Watney"}]

Deserialize JSON to list of mappings:

>>> import json
>>>
>>>
>>> DATA = """[
...     {"firstname": "Melissa", "lastname": "Lewis"},
...     {"firstname": "Rick", "lastname": "Martinez"},
...     {"firstname": "Mark", "lastname": "Watney"}]"""
>>>
>>>
>>> result = json.loads(DATA)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]


List of Sequences
-----------------
* ``json.dumps(data: list[Sequence]) -> str``
* ``json.loads(data: str) -> list[list]``

Serialize list of sequences to JSON:

>>> import json
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>>
>>> result = json.dumps(DATA)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"],
 [5.8, 2.7, 5.1, 1.9, "virginica"],
 [5.1, 3.5, 1.4, 0.2, "setosa"],
 [5.7, 2.8, 4.1, 1.3, "versicolor"]]

Deserialize JSON to list of sequences:

>>> import json
>>>
>>>
>>> DATA = """[
...     ["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"],
...     [5.8, 2.7, 5.1, 1.9, "virginica"],
...     [5.1, 3.5, 1.4, 0.2, "setosa"],
...     [5.7, 2.8, 4.1, 1.3, "versicolor"]]"""
>>>
>>>
>>> result = json.loads(DATA)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'],
 [5.8, 2.7, 5.1, 1.9, 'virginica'],
 [5.1, 3.5, 1.4, 0.2, 'setosa'],
 [5.7, 2.8, 4.1, 1.3, 'versicolor']]


Assignments
-----------
.. literalinclude:: assignments/json_tostring_a.py
    :caption: :download:`Solution <assignments/json_tostring_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_tostring_b.py
    :caption: :download:`Solution <assignments/json_tostring_b.py>`
    :end-before: # Solution
