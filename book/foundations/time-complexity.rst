**********************
Złożoność obliczeniowa
**********************

* https://wiki.python.org/moin/TimeComplexity
* https://visualgo.net/bn/sorting
* http://sorting.at/
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

Zastosowanie setów zamiast list
===============================
Jeżeli masz listę w której sprawdzasz czy element występuje, to zamień listę na ``set``, dzięki temu będzie lepsza złożoność

.. code-block:: python

    IMIONA = ['José', 'Ivan', 'Max']

    if imie in IMIONA:
        pass

.. code-block:: python

    IMIONA = {'José', 'Ivan', 'Max'}

    if imie in IMIONA:
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
    output = '\r\n'.join(html)

    print(output)

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