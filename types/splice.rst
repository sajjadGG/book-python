********
Splicing
********


Accessing element with index
============================

.. code-block:: python

    text = 'Lorem ipsum'

    text[0]             # 'L'
    text[2]             # 'r'
    text[-1]            # 'm'
    text[-3]            # 's'


Accessing range of elements
===========================
.. code-block:: python

    text = 'Lorem ipsum'

    text[0:3]             # 'Lor'
    text[:3]              # 'Lor'
    text[1:4]             # 'ore'
    text[-3:]             # 'sum'
    text[-3:-1]           # 'su'
    text[:-2]             # 'Lorem ips'

.. code-block:: python

    text = 'Lorem ipsum'
    lower = 1
    upper = 4

    text[lower:upper]     # 'ore'
    text[lower:upper+1]   # 'orem'


Splice
======
.. code-block:: python

    text = 'Lorem ipsum'
    RANGE = splice(1, 4)

    text[RANGE]           # 'ore'


Reversing and stepping over elements
====================================
.. code-block:: python

    text = 'Lorem ipsum'

    text[::2]             # 'Lrmism'
    text[::-1]            # 'muspi meroL'
    text[::-2]            # 'msimrL'


Assignments
===========
