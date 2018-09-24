.. _Slice:

*******
Slicing
*******


Accessing element with index
============================

.. code-block:: python

    text = 'That\'s one small step for [a] man, one giant leap for mankind.'

    text[0]             # 'T'
    text[2]             # 'a'
    text[4]             # "'"
    text[-1]            # '.'
    text[-3]            # 'n'
    text[100]           # IndexError: string index out of range


Accessing range of elements
===========================
.. code-block:: python

    text = 'That\'s one small step for [a] man, one giant leap for mankind.'

    text[0:3]             # 'Tha'
    text[:3]              # 'Tha'
    text[1:4]             # 'hat'
    text[-8:]             # 'mankind.'
    text[-8:-1]           # 'mankind'
    text[:-9]             # "That's one small step for [a] man, one giant leap for"
    text[:100]            # "That's one small step for [a] man, one giant leap for mankind."
    text[100:]            # ''

.. code-block:: python

    text = 'That\'s one small step for [a] man, one giant leap for mankind.'
    lower = 1
    upper = 6

    text[lower:upper]       # "hat's"
    text[lower:upper+1]     # "hat's "
    text[lower-1:upper+1]   # "That's "


Slice
=====
.. code-block:: python

    text = 'That\'s one small step for [a] man, one giant leap for mankind.'
    RANGE = slice(0, 6)

    text[RANGE]           # "That's"


Reversing and stepping over elements
====================================
.. code-block:: python

    text = 'Lorem ipsum'

    text[::2]             # "Ta' n ml tpfr[]mn n in epfrmnid"
    text[::-1]            # ".dniknam rof pael tnaig eno ,nam ]a[ rof pets llams eno s'tahT"
    text[::-2]            # '.nka o altageo,a a o eslaseosth'


Assignments
===========

Slicing text
------------
#. Z podanych poniżej ciągów znaków wytnij ``Jana III Sobieskiego``
#. Jakie parametry użyłeś dla każdej z linijek?

.. code-block:: python

    a = 'UL. Jana III Sobieskiego 1/2'
    b = 'ulica Jana III Sobieskiego 1/2'
    c = 'os. Jana III Sobieskiego 1/2'
    d = 'plac Jana III Sobieskiego 1/2'
    e = 'aleja Jana III Sobieskiego 1/2'
    f = 'alei Jana III Sobieskiego 1/2'
    g = 'Jana III Sobieskiego 1 m. 2'
    h = 'os. Jana III Sobieskiego 1 apt 2'


:About:
    * Filename: ``types_slice.py``
    * Lines of code to write: 8 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Wycinanie elementów stringów
    * Indeksacja elemntów
