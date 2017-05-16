Instrukcje warunkowe
====================

``if`` ... ``elif`` ... ``else``
--------------------------------

.. code-block:: python

    if ... :
         print('this is true')
     else:
         print('this is false')


.. code-block:: python

    if name != 'Agata':
         print('this is false')
     else:
         print('this is true')


.. code-block:: python

    if name == 'Agata':
        print('Your name is Agata')
    elif name == 'Borys':
        print('Your name is Borys')
    else:
         print('Your name is neither Boris nor Agata')

.. code-block:: python

    if not 0 <= k <= n:
        raise ValueError('Sample larger than population')


``not``, ``in``, ``is``
-----------------------

.. code-block:: python

    if name in ['Agata', 'Boris']:
        print('Your name is Agata or Boris')
    else:
         print('Your name is neither Boris nor Agata')


.. code-block:: python

    if not name == 'Agata':
         print('this is false')
     else:
         print('this is true')

.. code-block:: python

    if not name:
         print('Name is not set')
     else:
         print('You have set your name')


.. code-block:: python

    if name is None:
         print('Name is not set')
     else:
         print('You have set your name')


``switch`` statement?
---------------------
* Why ``switch`` is bad practise?

.. code-block:: python

    if name == 'Agata':
        print('Your name is Agata')
    elif name == 'Borys':
        print('Your name is Borys')
    elif name == 'Matt':
        print('Your name is Borys')
    else:
         print('Your name is other')


.. code-block:: python

    def f(x):
        return {
            'a': 1,
            'b': 2,
        }[x]

.. code-block:: python

    choices = {'a': 1, 'b': 2}
    result = choices.get(key, 'default')


Zadania kontrolne
=================

Dzienniczek ucznia
------------------

:Nazwa skryptu: ``bin/oceny.py``
:Uruchamianie: ``python bin/oceny.py``

:Zadanie:
    Napisz program, który wczytuje od użytkownika kolejne oceny i:

    * sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen
    * jeżeli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją do dzienniczka
    * jeżeli wpisano cyfrę nie znjadującą się na liście dopuszczalnych ocen, wyświetl informację i zakończ wpisywanie
    * wyświetla wyliczoną dla dzienniczka ocen średnią arytmetyczną
    * jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka
    * wykorzystaj moduł statistics do wyliczania średniej

:Warunek:
    * Zastosuj akademicką skalę ocen ``[2, 3, 3.5, 4, 4.5, 5]``

:Podpowiedź:
    * dla ułatwienia wszystkie oceny mogą być typu ``float``
    * ``len()`` ``sum()``
    * ``in``
    * ``import statistics`` ``statistics.mean()``
