.. _Slice:

*******
Slicing
*******


Accessing element with index
============================

.. code-block:: python

    text = 'Lorem ipsum'

    text[0]             # 'L'
    text[2]             # 'r'
    text[-1]            # 'm'
    text[-3]            # 's'
    text[60]            # IndexError: string index out of range


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
    text[0:60]            # 'Lorem ipsum'
    text[60:]             # ''

.. code-block:: python

    text = 'Lorem ipsum'
    lower = 1
    upper = 4

    text[lower:upper]     # 'ore'
    text[lower:upper+1]   # 'orem'


Slice
=====
.. code-block:: python

    text = 'Lorem ipsum'
    RANGE = slice(1, 4)

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

Slicing text
------------
#. Z podanych poniżej ciągów znaków wytnij ``Jana III Sobieskiego``
#. Jakie parametry użyłeś dla każdej z linijek?

.. code-block:: text

    'UL. Jana III Sobieskiego 1/2'
    'ulica Jana III Sobieskiego 1/2'
    'os. Jana III Sobieskiego 1/2'
    'plac Jana III Sobieskiego 1/2'
    'aleja Jana III Sobieskiego 1/2'
    'alei Jana III Sobieskiego 1/2'
    'Jana III Sobieskiego 1 m. 2'
    'os. Jana III Sobieskiego 1 apt 2'
