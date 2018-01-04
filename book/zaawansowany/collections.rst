***********
Collections
***********

* https://docs.python.org/3/library/collections.html

It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

    ================  ====================================================================
    Name              Description
    ----------------  --------------------------------------------------------------------
    ``namedtuple()``  factory function for creating tuple subclasses with named fields
    ``deque``         list-like container with fast appends and pops on either end
    ``ChainMap``      dict-like class for creating a single view of multiple mappings
    ``Counter``       dict subclass for counting hashable objects
    ``OrderedDict``   dict subclass that remembers the order entries were added
    ``defaultdict``   dict subclass that calls a factory function to supply missing values
    ``UserDict``      wrapper around dictionary objects for easier dict subclassing
    ``UserList``      wrapper around list objects for easier list subclassing
    ``UserString``    wrapper around string objects for easier string subclassing
    ================  ====================================================================

``namedtuple``
--------------

.. code-block:: python

    >>> # Basic example
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
    >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
    33
    >>> x, y = p                # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y               # fields also accessible by name
    33
    >>> p                       # readable __repr__ with a name=value style
    Point(x=11, y=22)
