.. _Indexes:

*******
Indexes
*******


Accessing element with index
============================
* Index must be positive or negative ``int``
* Index must be less or equal to length of object
* Negative index starts from the end and go right to left


Accessing element from start
============================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0]         # 'W'
    text[1]         # 'e'
    text[23]        # 'M'


Accessing element from back
===========================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[-1]        # '!'
    text[-5]        # 'M'


Accessing not existing element
==============================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[100]
    # IndexError: string index out of range


Assignments
===========
.. todo:: Create Assignments
