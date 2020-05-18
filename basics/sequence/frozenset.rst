**********************
Sequence ``frozenset``
**********************


.. highlights::
    * Only unique values
    * Immutable - cannot add, modify or remove items
    * Can store elements of any **hashable** types
    * Has all ``set`` methods such as ``.intersect()``, ``.subset()`` ``.union()``, etc.
    * One solid block in memory


Type Definition
===============
.. highlights::
    * Set is ordered data structure
    * Do not support indexing
    * Do not support slicing
    * Defining only with ``frozenset()`` - no short syntax
    * Comma after last element is optional
    * Brackets are required

.. code-block:: python
    :caption: ``set`` type definition

    data = frozenset()

    data = frozenset({1})
    data = frozenset({1, 2, 3})
    data = frozenset({1.1, 2.2, 3.3})
    data = frozenset({True, False})
    data = frozenset({'a', 'b', 'c'})
    data = frozenset({'a', 1, 2.2, True, None})


Type Casting
============
* ``frozenset()`` converts argument to ``frozenset``

.. code-block:: python

    data = [1, 2, 3]
    frozenset(data)
    # frozenset({1, 2, 3})

.. code-block:: python

    data = (1, 2, 3)
    frozenset(data)
    # frozenset({1, 2, 3})

.. code-block:: python

    data = {1, 2, 3}
    frozenset(data)
    # frozenset({1, 2, 3})

.. code-block:: python

    data = frozenset({1, 2, 3})
    frozenset(data)
    # frozenset({1, 2, 3})

.. code-block:: python

    data = [1, 2, 3, [4, 5]]
    frozenset(data)
    # TypeError: unhashable type: 'list'

.. code-block:: python

    data = [1, 2, 3, (4, 5)]
    frozenset(data)
    # frozenset({(4, 5), 1, 2, 3})


``frozenset`` or ``set``
========================
Both:

    * unique elements
    * only **hashable** elements

Frozenset:

    * ordered
    * immutable
    * one contingent block of data in memory

Set:

    * unordered
    * mutable
    * implemented in memory as list of pointers to objects
    * objects are scattered in memory
