.. _Loop While:

**************
Loop ``while``
**************


Syntax
======
.. highlights::
    * Continue execution when argument is ``True``
    * Stops if argument is ``False``

.. code-block:: python
    :caption: ``while`` loop generic syntax

    while <CONDITION>:
        ...


Use Cases
=========

Never ending loop
-----------------
.. code-block:: python
    :caption: Never ending loop

    while True:
        print('hello')

Stop conditions
---------------
.. code-block:: python
    :caption: Stop conditions

    i = 0

    while i < 3:
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
    :caption: Iterating over sequence

    i = 0
    data = ['a', 'b', 'c']

    while i < len(data):
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
    :caption: Exit flag

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
    :caption: Skipping iterations using ``continue`` keyword

    i = 0

    while i < 10:
        print(i, end=', ')
        i += 1

        if i % 3:
            continue
        else:
            print(end='\n')

    # 0, 1, 2,
    # 3, 4, 5,
    # 6, 7, 8,
    # 9,

Exiting the loop
----------------
.. code-block:: python
    :caption: Exiting the loop using ``break`` keyword

    while True:
        number = input('Type number: ')

        if not number:
            # if user hit enter
            # without typing a number
            break


Assignments
===========

Report card
-----------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/loop_while_report_card.py`

:English:
    #. Use data from "Input" section (see below)
    #. Convert ``DATA`` to ``List[float]`` using ``while`` loop and name it ``grade_scale``
    #. Ask user about grade, one at a time
    #. User will type only valid ``int`` or ``float``
    #. If grade is on a new grade scale - add it to report card
    #. If grade is not on a new grade scale - print "Grade is not allowed" and continue input
    #. If user pressed Enter key, end inserting data
    #. At the end, print calculated mean
    #. Test case when report list is empty

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj ``DATA`` do ``List[float]`` używając pętli ``while`` i nazwij ``grade_scale``
    #. Poproś użytkownika o ocenę, jedną na raz
    #. Użytkownik poda tylko poprawne ``int`` lub ``float``
    #. Jeżeli ocena jest na nowej skali - dodaj ją do dzienniczka
    #. Jeżeli oceny nie ma na liście - wyświetl "Grade is not allowed" i kontynuuj wpisywanie
    #. Jeżeli użytkownik wcisnął Enter, zakończ wprowadzanie danych
    #. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną
    #. Przetestuj przypadek, gdy dzienniczek jest pusty

:Input:
    .. code-block:: python

        DATA = (2, 3, 3.5, 4, 4.5, 5)

:The whys and wherefores:
    * Reading user input
    * Input validation
    * Type casting
    * Sequences
    * Using while loop
    * Breaking loop
    * Using built-in functions

:Hints:
    * ``input(...)``
    * ``mean = sum(...) / len(...)``
