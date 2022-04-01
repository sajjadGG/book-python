JSON File
=========
* file extension ``.json``
* ``json.load(file) -> dict``
* ``json.dump(data, file) -> None``


Write
-----
.. code-block:: text

    def dump(obj: Any,
             fp: IO[str],
             *,
             skipkeys: bool = ...,
             ensure_ascii: bool = ...,
             check_circular: bool = ...,
             allow_nan: bool = ...,
             cls: Type[JSONEncoder] | None = ...,
             indent: None | int | str = ...,
             separators: tuple[str, str] | None = ...,
             default: (Any) -> Any | None = ...,
             sort_keys: bool = ...,
             **kwds: Any) -> None

Serialize to JSON:

>>> import json
>>>
>>>
>>> FILE = r'/tmp/myfile.json'
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney'}
>>>
>>>
>>> with open(FILE, mode='w') as file:
...     json.dump(DATA, file)
>>>
>>> result = open(FILE).read()
>>> print(result)
{"firstname": "Mark", "lastname": "Watney"}


Read
----
.. code-block:: text

    def load(fp: SupportsRead[str | bytes],
             *,
             cls: Type[JSONDecoder] | None = ...,
             object_hook: (dict) -> Any | None = ...,
             parse_float: (str) -> Any | None = ...,
             parse_int: (str) -> Any | None = ...,
             parse_constant: (str) -> Any | None = ...,
             object_pairs_hook: (list[tuple[Any, Any]]) -> Any | None = ...,
             **kwds: Any) -> Any

Serialize to JSON:

>>> import json
>>>
>>>
>>> FILE = r'/tmp/myfile.json'
>>> DATA = '{"firstname": "Mark", "lastname": "Watney"}'
>>> _ = open(FILE, mode='w').write(DATA)
>>>
>>>
>>> with open(FILE) as file:
...     result = json.load(file)
>>>
>>> print(result)
{'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
-----------
.. literalinclude:: assignments/json_file_a.py
    :caption: :download:`Solution <assignments/json_file_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_file_b.py
    :caption: :download:`Solution <assignments/json_file_b.py>`
    :end-before: # Solution
