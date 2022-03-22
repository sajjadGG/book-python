Protocol About
==============
* ``Container``
* ``Hashable``
* ``Iterable``
* ``Iterator``
* ``Reversible``
* ``Generator``
* ``Callable``
* ``Collection``
* ``Sequence``
* ``MutableSequence``
* ``ByteString``
* ``Set``
* ``MutableSet``
* ``Mapping``
* ``MutableMapping``
* ``MappingView``
* ``ItemsView``
* ``KeysView``
* ``ValuesView``
* ``Awaitable``
* ``Coroutine``
* ``AsyncIterator``
* ``AsyncGenerator``


About
-----
.. csv-table:: Protocols
    :header: "Abstract Base Class", "Inherits from", "Methods"
    :widths: 15, 15, 60

    "Container",           "",                           "``__contains__``"
    "Hashable",            "",                           "``__hash__``"
    "Iterable",            "",                           "``__iter__``"
    "Iterator",            "Iterable",                   "``__next__``, ``__iter__``"
    "Reversible",          "Iterable",                   "``__reversed__``"
    "Generator",           "Iterator",                   "``send``, ``throw``, ``close``, ``__iter__``, ``__next__``, ``__len__``"
    "Callable",            "",                           "``__call__``"
    "Collection",          "Sized, Iterable, Container", "``__contains__``, ``__iter__``, ``__len__``"
    "Sequence",            "Reversible, Collection",     "``__getitem__``, ``__contains__``, ``__iter__``, ``__reversed__``, ``__len__``, ``index``, ``count``"
    "MutableSequence",     "Sequence",                   "``__getitem__``, ``__setitem__``, ``append``, ``reverse``, ``extend``, ``pop``, ``__delitem__``, ``remove``, ``__iadd__``, ``__len__``, ``insert``, ``__contains__``, ``__iter__``, ``__reversed__``, ``index``, ``count``"
    "ByteString",          "Sequence",                   "``__getitem__``, ``__len__``, ``__contains__``, ``__iter__``, ``__reversed__``, ``index``, ``count``"
    "Set",                 "Collection",                 "``__contains__``, ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``, ``__iter__``, ``__gt__``, ``__ge__``, ``__and__``, ``__or__``, ``__len__``, ``__sub__``, ``__xor__``, ``isdisjoint``"
    "MutableSet",          "Set",                        "``__contains__``, ``__iter__``, ``clear``, ``pop``, ``remove``, ``__ior__``, ``__len__``, ``__iand__``, ``__ixor__``, ``__isub__``, ``add``, ``discard``, ``__contains__``, ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``, ``__iter__``, ``__gt__``, ``__ge__``, ``__and__``, ``__or__``, ``__len__``, ``__sub__``, ``__xor__``, ``isdisjoint``"
    "Mapping",             "Collection",                 "``__getitem__``, ``__contains__``, ``keys``, ``items``, ``values``, ``__iter__``, ``get``, ``__eq__``, ``__ne__``, ``__len__``"
    "MutableMapping",      "Mapping",                    "``__getitem__``, ``__setitem__``, ``pop``, ``popitem``, ``clear``, ``update``, ``__delitem__``, ``setdefault``, ``__iter__``, ``__len__``, ``__getitem__``, ``__contains__``, ``keys``, ``items``, ``values``, ``__iter__``, ``get``, ``__eq__``, ``__ne__``, ``__len__``"
    "MappingView",         "Sized",                      "``__len__``"
    "ItemsView",           "MappingView, Set",           "``__contains__``, ``__iter__``"
    "KeysView",            "MappingView, Set",           "``__contains__``, ``__iter__``"
    "ValuesView",          "MappingView, Collection",    "``__contains__``, ``__iter__``"
    "Awaitable",           "",                           "``__await__``"
    "Coroutine",           "Awaitable, AsyncIterable",   "``send``, ``throw``, ``close``, ``__aiter__``"
    "AsyncIterator",       "AsyncIterable",              "``__anext__``, ``__aiter__``"
    "AsyncGenerator",      "AsyncIterator",              "``asend``, ``athrow``, ``aclose``, ``__aiter__``, ``__anext__``"
