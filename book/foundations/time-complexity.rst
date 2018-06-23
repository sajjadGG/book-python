***************
Time Complexity
***************


* https://wiki.python.org/moin/TimeComplexity
* https://visualgo.net/bn/sorting
* http://sorting.at/
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html


Zastosowanie setów zamiast list
===============================
Jeżeli masz listę w której sprawdzasz czy element występuje, to zamień listę na ``set``, dzięki temu będzie lepsza złożoność

.. code-block:: python

    NAMES = ['José', 'Ivan', 'Max']

    if 'Max' in NAMES:
        pass

.. code-block:: python

    NAMES = {'José', 'Ivan', 'Max'}

    if 'Max' in NAMES:
        pass


Zastosowanie list zamiast konkatanacji stringów
===============================================
.. code-block:: python

    # Performance - Method concatenates strings using + in a loop
    html = '<table>'

    for element in lista:
        html += f'<tr><td>{element}</td></tr>'
    html += '</table>'

    print(html)

.. code-block:: python

    # Problem solved
    html = ['<table>']

    for element in lista:
        html.append(f'<tr><td>{element}</td></tr>')

    html.append('</table>')
    print(''.join(html))


Inne
====
* Jeżeli coś ``collections.deque`` - Double ended Queue
* Serializowane kolejki przy wielowątkowości
* Uwaga na set zawierający floaty, bo pomiędzy dwoma wartościami jest nieskończona ilość wyrażeń

.. code-block:: python

    range(0, 2)
    # 0
    # 1
    # 2
    # 3
    # 4

    range(0.0, 5.0)

Assignments
===========

Memoization
-----------
#. Napisz program, który obliczy silnię dla dowolnego ``int``
#. Program ma zapisać w ``dict`` o nazwie ``MEMOIZE`` wyniki funkcji dla poszczególnych parametrów (klucz to parametr, a wartość to wynik)
#. Przed uruchomieniem funkcji, musi sprawdzić czy wynik został już wcześniej obliczony

    - jeżeli tak, to zwraca dane z cache
    - jeżeli nie, to oblicza, aktualizuje cache a następnie zwraca wartość

#. Porównaj prędkość działania z obliczaniem na bieżąco dla parametru 500

:Założenia:
    * Nazwa pliku: ``functions-memoize.py``
    * Szacunkowa długość kodu: około 5 linii
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź:
    .. code-block:: python

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
