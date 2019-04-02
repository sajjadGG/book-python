******************
``set`` arithmetic
******************


``set.isdisjoint()``
====================
* Return ``True`` if the ``set`` has no elements in common with other
* Sets are disjoint if and only if their intersection is the empty ``set``.

.. code-block:: python

    {1,2}.isdisjoint({3,4})     # True


``set.issubset()``
==================
* Test whether every element in the ``set`` is in other

.. code-block:: python

    {1,2} <= {3,4}              # False

.. code-block:: python

    {1,2} <= {1,2}              # True
    {1,2} <= {1,2,3}            # True

.. code-block:: python

    {1,2} < {1,2,3}             # True
    {1,2} < {1,2}               # False


``set.issuperset()``
====================
* Test whether every element in other is in the ``set``

.. code-block:: python

    {1,2} > {1,2,3}             # False
    {1,2} > {1,2}               # False
    {1,2,3} > {1,2}             # True

.. code-block:: python

    {1,2} >= {1,2}              # True
    {1,2,3} >= {1,2}            # True


``set.union()``
===============
* Return a new ``set`` with elements from the ``set`` and all others

.. code-block:: python

    {1,2} | {1,2}               # {1, 2}
    {1,2,3} | {1,2}             # {1, 2, 3}
    {1,2,3} | {1,2,4}           # {1, 2, 3, 4}
    {1,2} | {1,3} | {2,4}       # {1, 2, 3, 4}


``set.intersection()``
======================
* Return a new ``set`` with elements common to the ``set`` and all others

.. code-block:: python

    {1,2} & {2,3}               # {2}
    {1,2} & {2,3} & {2,4}       # {2}
    {1,2} & {2,3} & {3}         # set()


``set.difference()``
====================
* Return a new ``set`` with elements in the ``set`` that are not in the others

.. code-block:: python

    {1,2} - {2,3}               # {1}
    {1,2} - {2,3} - {3}         # {1}
    {1,2} - {1,2,3}             # set()


``set.symmetric_difference()``
==============================
* Return a new set with elements in either the set or other but not both

.. code-block:: python

    {1,2} ^ {1,2}               # set()
    {1,2} ^ {2,3}               # {1, 3}
    {1,2} ^ {1,3}               # {2, 3}
