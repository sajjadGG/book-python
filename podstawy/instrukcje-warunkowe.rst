.. _Instrukcje warunkowe:

********************
Instrukcje warunkowe
********************

``if`` ... ``elif`` ... ``else``
================================

.. code-block:: python

    if ... :
         print('this is true')
     else:
         print('this is false')


.. code-block:: python

    if name != 'José Jiménez':
         print('this is false')
     else:
         print('this is true')


.. code-block:: python

    if name == 'José Jiménez':
         print('My name José Jiménez')
    elif name == 'Max Peck':
        print('Your name is Max Peck')
    else:
         print('Your name is neither José Jiménez nor Max Peck')

.. code-block:: python

    if not 0 <= k <= n:
        raise ValueError('Sample larger than population')


``not``, ``in``, ``is``
=======================

.. code-block:: python

    if name in ['José Jiménez', 'Max Peck']:
        print('Your name is José Jiménez or Max Peck')
    else:
         print('Your name is neither José Jiménez nor Max Peck')


.. code-block:: python

    if not name == 'José Jiménez':
         print('Not José')
     else:
         print('My name José Jiménez')

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
=====================
* Why ``switch`` is bad practise?

.. code-block:: python

    if name == 'José Jiménez':
        print('My name José Jiménez')
    elif name == 'Ivan Ivanovic':
        print('Your name is Ivan Ivanovic')
    elif name == 'Max Peck':
        print('Your name is Max Peck')
    else:
         print('Your name is other')


.. code-block:: python

    def switch(x):
        return {
            'a': 1,
            'b': 2,
        }[x]


    switch['a']

.. code-block:: python

    choices = {'a': 1, 'b': 2}
    result = choices.get(key, 'default')


Zadania kontrolne
=================

Dzienniczek ucznia
------------------
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
    * ``statistics.mean()``
