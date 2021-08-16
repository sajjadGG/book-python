FuncProg Immutable
==================


Rational
--------
* Purely functional data structures have persistence (keeps previous
  versions of the data structure unmodified)

* The array with constant access and update times is a basic component of
  most imperative languages, and many imperative data-structures, such as
  the hash table and binary heap, are based on arrays

* Arrays can be replaced by maps or random access lists, which admit
  purely functional implementation, but have logarithmic access and update
  times

* Source: [#WikipediaFunc]_


Immutable Types
---------------
* ``int``
* ``float``
* ``complex``
* ``bool``
* ``None``
* ``str``
* ``bytes``
* ``tuple``
* ``frozenset``
* ``mappingproxy``


Mutable Types
-------------
* ``list``
* ``set``
* ``dict``


Comparison
----------
.. csv-table:: Comparison
    :header: Immutable, Mutable
    :widths: 50, 50

    int          ,
    float        ,
    complex      ,
    bool         ,
    None         ,
    str          ,
    bytes        , bytearray
    tuple        , list
    frozenset    , set
    mappingproxy , dict
    NamedTuple   ,
    namedtuple   ,
                 , array
                 , TypedDict
    dataclass    , dataclass
