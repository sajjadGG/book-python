**************
``while`` loop
**************


Syntax
======
* Continue execution when argument is ``True``

Generic syntax
--------------
.. code-block:: python
    :caption: ``while`` loop generic syntax

    while CONDITION:
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
* Better idea for this is to use ``for`` loop
* ``for`` loop supports Iterators
* ``len()`` must write all ``numbers`` to memory, to calculate its length

.. code-block:: python

    i = 0
    numbers = [1, 2, 3]

    while i <= len(numbers):
        current = numbers[i]
        print(current)
        i += 1

    # 1
    # 2
    # 3

Exit flag
---------
* Exit flag pattern is useful if you have for example multi-threaded application

.. code-block:: python

    i = 0
    abort = False

    while not abort:
        print(i)
        i += 1

        if i % 3 == 0:
            print('Aborting!')
            abort = True

    # 0
    # 1
    # 2
    # Aborting!


``break`` and ``continue``
==========================

Skipping iterations
-------------------
* if ``continue`` is encountered, it will jump to next loop iteration
.. code-block:: python

    i = 0

    while i <= 10:
        i += 1

        if i % 2 == 0:
            continue

        print(i)

    # 1
    # 3
    # 5

Exiting the loop
----------------
.. code-block:: python

    while True:
        number = input('Type number: ')

        # if user hit enter, without typing number
        if not number:
            break


``else``
========
* ``else`` will execute, if ``break`` was not used to exit the loop

.. code-block:: python

    abort = False
    countdown = 10

    while countdown >= 0:
        if abort:
            break

        print(f'Launch in T-{countdown}')
        i -= 1
    else:
        print('There was no abort this time')
        print('Launch rocket')


Assignments
===========

Report card
-----------
* Filename: ``loop_report_card.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Do zmiennej zapisz skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)``
#. Za pomocą pętli ``while`` przekonwertuj skalę na zmienną typu ``List[float]``
#. Użytkownik podaje oceny jako ``int`` lub ``float``, nie będzie próbował podawać niepoprawnych typów, np. ``str`` albo ``float`` z przecinkiem zamiast kropki
#. Jeżeli wciśnięto sam Enter, zakończ wpisywanie do dzienniczka
#. Jeżeli ocena na liście dopuszczalnych ocen:

    - Jest: dodaj ją do dzienniczka
    - Nie ma: wyświetl informację "Grade is not allowed" i dalej kontynuuj wpisywanie

#. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną z ocen

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Generowanie struktur danych i konwersja typów
    * Weryfikacja ciągu wprowadzonego od użytkownika
    * Korzystanie z pętli oraz instrukcji wychodzących
    * Konwersja typów i rzutowanie
    * Sprawdzanie czy obiekt jest instancją klasy
    * Wykorzystanie funkcji wbudowanych

:Hints:
    * ``average = sum(...) / len(...)``
