.. _Loop While:

**************
Loop ``while``
**************


Syntax
======
.. highlights::
    * Continue execution when argument is ``True``
    * Stops if argument is ``False``

Generic syntax
--------------
.. code-block:: python
    :caption: ``while`` loop generic syntax

    while <CONDITION>:
        ...


Example
=======

Never ending loop
-----------------
.. code-block:: python

    while True:
        print('hello')

Stop conditions
---------------
.. code-block:: python

    i = 0

    while i <= 3:
        print(i)
        i += 1

    # 0
    # 1
    # 2

Iterating over sequence
-----------------------
.. highlights::
    * Better idea for this is to use ``for`` loop
    * ``for`` loop supports Iterators
    * ``len()`` must write all ``numbers`` to memory, to calculate its length

.. code-block:: python

    i = 0
    data = ['a', 'b', 'c']

    while i <= len(data):
        print(data[i])
        i += 1

    # 'a'
    # 'b'
    # 'c'

Exit flag
---------
.. highlights::
    * Exit flag pattern is useful if you have for example multi-threaded application

.. code-block:: python

    i = 10
    abort = False

    while not abort:
        print(i)
        i -= 1

        if i == 6:
            print('Abort, Abort, Abort!')
            abort = True

    # 10
    # 9
    # 8
    # 7
    # Abort, Abort, Abort!


``break`` and ``continue``
==========================

Skipping iterations
-------------------
.. highlights::
    * if ``continue`` is encountered, it will jump to next loop iteration

.. code-block:: python

    i = 0

    while i < 10:
        print(i, end=', ')
        i += 1

        if i % 2 == 0:
            continue

        print()

    # 0,
    # 1, 2,
    # 3, 4,
    # 5, 6,
    # 7, 8,
    # 9,

Exiting the loop
----------------
.. code-block:: python

    while True:
        number = input('Type number: ')

        # if user hit enter, without typing number
        if not number:
            break


Assignments
===========

Report card
-----------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/while_report_card.py`

:English:
    #. For given grade scale in input data (see below)
    #. Convert scale to ``List[float]`` using ``while`` loop
    #. Ask user about grade, one at a time
    #. User will type only valid ``int`` or ``float``
    #. If grade is on a new grade scale - add it to report card
    #. If grade is not on a new grade scale - print "Grade is not allowed" and continue input
    #. If user pressed Enter key, end inserting data
    #. At the end, print calculated mean
    #. Test case when report list is empty

:Polish:
    #. Dla skali ocen w danych wejściowych (patrz sekcja input)
    #. Przekonwertuj skalę do ``List[float]`` używając pętli ``while``
    #. Poproś użytkownika o ocenę, jedną na raz
    #. Użytkownik poda tylko poprawne ``int`` lub ``float``
    #. Jeżeli ocena jest na nowej skali - dodaj ją do dzienniczka
    #. Jeżeli oceny nie ma na liście - wyświetl "Grade is not allowed" i kontynuuj wpisywanie
    #. Jeżeli użytkownik wcisnął Enter, zakończ wprowadzanie danych
    #. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną
    #. Przetestuj przypadek, gdy dzienniczek jest pusty

:Input:
    .. code-block:: python

        INPUT = (2, 3, 3.5, 4, 4.5, 5)

:The whys and wherefores:
    * Reading user input
    * Input validation
    * Type casting
    * Sequences
    * Using while loop
    * Breaking loop
    * Using built-in functions

:Hints:
    * ``input('...')``
    * ``mean = sum(...) / len(...)``
