***************
``set`` Methods
***************


``set.isdisjoint()``
====================
* No common elements

.. code-block:: python

    {1,2}.isdisjoint({3,4})     # True


``set.issubset()``
==================
* All elements in both

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
* All elements of ``b`` are in ``a``

.. code-block:: python

    {1,2} > {1,2,3}             # False
    {1,2} > {1,2}               # False
    {1,2,3} > {1,2}             # True

.. code-block:: python

    {1,2} >= {1,2}              # True
    {1,2,3} >= {1,2}            # True


``set.union()``
===============
* add

.. code-block:: python

    {1,2} | {1,2}               # {1, 2}
    {1,2,3} | {1,2}             # {1, 2, 3}
    {1,2,3} | {1,2,4}           # {1, 2, 3, 4}
    {1,2} | {1,3} | {2,4}       # {1, 2, 3, 4}


``set.difference()``
====================
* subtract

.. code-block:: python

    {1,2} - {2,3}               # {1}
    {1,2} - {2,3} - {3}         # {1}
    {1,2} - {1,2,3}             # set()


``set.symmetric_difference()``
==============================
* not common elements from each

.. code-block:: python

    {1,2} ^ {1,2}               # set()
    {1,2} ^ {2,3}               # {1, 3}
    {1,2} ^ {1,3}               # {2, 3}


``set.intersection()``
======================
* common element from each

.. code-block:: python

    {1,2} & {2,3}               # {2}
    {1,2} & {2,3} & {2,4}       # {2}
    {1,2} & {2,3} & {3}         # set()


Assignments
===========
.. todo:: Create assignments
