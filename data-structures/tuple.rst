*********
``tuple``
*********


* Can store elements of any types
* Immutable - cannot add, modify or remove items


Initializing
============
* ``tuple()`` is more readable
* ``()`` is used more often

Initialize empty
----------------
.. code-block:: python

    my_tuple = ()
    my_tuple = tuple()

Initialize with one element
---------------------------
* Single element ``tuple`` require comma at the end (**important!**)
* Brackets are optional

.. code-block:: python

    my_tuple = 1,
    my_tuple = (1,)

Initialize with many elements
-----------------------------
* Comma after last element is optional
* Brackets are optional

.. code-block:: python

    my_tuple = 1, 2
    my_tuple = (1, 2)

.. code-block:: python

    my_tuple = 1, 2.0, None, False, 'José'
    my_tuple = (1, 2.0, None, False, 'José')


Length of a ``tuple``
=====================
.. code-block:: python

    my_tuple = (1, 2, 3)

    len(my_tuple)           # 3


Assignments
===========
.. todo:: Create Assignments
