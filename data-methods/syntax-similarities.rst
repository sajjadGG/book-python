*******************
Syntax similarities
*******************


``dict`` and ``set``
====================
* Both ``set`` and ``dict`` keys must be hashable
* Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
* Despite similar syntax, they are different types

.. code-block:: python

    {}                # dict
    {1}               # set

    {1: 2}            # dict
    {1, 2}            # set

    {1: 2,}           # dict
    {1, 2,}           # set

    {1: 2, 3: 4}      # dict
    {1, 2, 3, 4}      # set

Empty ``dict``
--------------
.. code-block:: python

    my_data = {1: 1}
    # {1:1}

    my_data.pop(1)
    # {}

Empty ``set``
-------------
.. code-block:: python

    my_data = {1}
    # {1}

    my_data.pop()
    # set()

Differences
-----------
.. code-block:: python

    my_data = {}
    isinstance(my_data, dict)         # True
    isinstance(my_data, set)          # False

    my_data = {1}
    isinstance(my_data, dict)         # False
    isinstance(my_data, set)          # True

    my_data = {1: 1}
    isinstance(my_data, dict)         # True
    isinstance(my_data, set)          # False


``tuple`` vs. ``str``
=====================
.. code-block:: python

    what = 'foo'      # str
    what = 'foo',     # tuple with str
    what = 'foo'.     # SyntaxError: invalid syntax

.. code-block:: python

    what = ('foo')    # str
    what = ('foo',)   # tuple with str
    what = ('foo'.)   # SyntaxError: invalid syntax

``tuple`` vs. ``float`` and ``int``
-----------------------------------
.. code-block:: python

    what = 1.2        # float
    what = 1,2        # tuple with two int

    what = (1.2)      # float
    what = (1,2)      # tuple with two int

.. code-block:: python

    what = 1.2,       # tuple with float
    what = 1,2.3      # tuple with int and float

    what = (1.2,)     # tuple with float
    what = (1,2.3)    # tuple with int and float

.. code-block:: python

    what = 1.         # float
    what = .5         # float
    what = 1.0        # float
    what = 1          # int

    what = (1.)       # float
    what = (.5)       # float
    what = (1.0)      # float
    what = (1)        # int

.. code-block:: python

    what = 10.5       # float
    what = 10,5       # tuple with two ints
    what = 10.        # float
    what = 10,        # tuple with int
    what = 10         # int

    what = (10.5)     # float
    what = (10,5)     # tuple with two ints
    what = (10.)      # float
    what = (10,)      # tuple with int
    what = (10)       # int

.. code-block:: python

    what = 1.,1.      # tuple with two floats
    what = .5,.5      # tuple with two floats
    what = 1.,.5      # tuple with two floats

    what = (1.,1.)    # tuple with two floats
    what = (.5,.5)    # tuple with two floats
    what = (1.,.5)    # tuple with two floats


Assignments
===========
.. todo:: Create assignments
