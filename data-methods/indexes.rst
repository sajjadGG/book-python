.. _Indexes:

*******
Indexes
*******


Accessing element with index
============================
* Index must be positive or negative ``int`` or zero
* Index must be less or equal to length of object
* Negative index starts from the end and go right to left


Indexing from start
-------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0]         # 'W'
    text[1]         # 'e'
    text[23]        # 'M'

Indexing from the end
---------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[-1]        # '!'
    text[-5]        # 'M'

Accessing not existing element
------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[100]
    # IndexError: string index out of range


Indexing data structures
========================

Indexing ``str``
----------------
.. code-block:: python

    DATA = 'abcde'

    DATA[2]             # 'c'
    DATA[-1]            # 'e'

Indexing ``list``
--------------------
* Indexes works the same like for ``str``

.. code-block:: python

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[1]             # 'b'
    DATA[-2]            # 'd'

Indexing ``tuple``
--------------------
* Indexes works the same like for ``str``

.. code-block:: python

    DATA = ('a', 'b', 'c', 'd', 'e')

    DATA[1]             # 'b'
    DATA[-2]            # 'd'

Indexing ``set``
----------------
* Indexes on ``set`` are not possible

.. code-block:: python

    DATA = {'a', 'b', 'c', 'd', 'e'}

    DATA[1]
    # TypeError: 'set' object is not subscriptable

Indexing ``dict``
-----------------
* Indexes on ``dict`` are not possible

.. code-block:: python

    DATA = {
        'a': 1,
        'b': 2,
    }

    DATA[1]
    # KeyError: 1

.. code-block:: python

    DATA = {
        1: 'a',
        2: 'b',
    }

    DATA[1]
    # 'a'


Assignments
===========
.. todo:: Create Assignments
