**********************
Conditional Statements
**********************


``if``
======
* The same indent level

Simple syntax
-------------
.. code-block:: python

    if True:
        print('First line of the true statement')

Multiline blocks
----------------
.. code-block:: python

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')
        print('Third line of the true statement')

Positive and negative values
----------------------------
Negative values:

    * ``False``
    * ``None``
    * ``0``
    * ``0.0``
    * ``0+0j``
    * ``0.0+0.0j``
    * empty ``str()`` or ``''``
    * empty ``tuple()`` or ``()``
    * empty ``dict()`` or ``{}``
    * empty ``list()`` or ``[]``
    * empty ``set()``

Positive values:

    * any other

Checking for simple value
-------------------------
.. code-block:: python

    name = 'José Jiménez'

    if name == 'José Jiménez':
        print('My name... José Jiménez')

Checking if value is in range
-----------------------------
.. code-block:: python

    age = 7

    if 0 <= age < 18:
        print('Age is between [0, 18)')

Checking if has value
---------------------
* More advanced examples will be covered latter

.. code-block:: python

    name = None

    if name:
        print(f'My name... {name}')
    else:
        print('Name is not defined')


``else``
========
* Optional
* Executed when condition is not met

Checking if variable is certain value
-------------------------------------
.. code-block:: python

    name = 'José Jiménez'

    if name == 'José Jiménez':
        print('My name... José Jiménez')
    else:
        print('Your name is different')

Multiline blocks
----------------
.. code-block:: python

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')
        print('Third line of the true statement')
    else:
        print('First line of the false statement')
        print('Second line of the false statement')
        print('Third line of the false statement')


Inline ``if``
=============
.. code-block:: python
    :caption: Normal ``if``

    ip = '127.0.0.1'

    if '.' in ip:
        protocol = 'IPv4'
    else:
        protocol = 'IPv6'

.. code-block:: python
    :caption: One line version

    ip = '127.0.0.1'

    protocol = 'IPv4' if '.' in ip else 'IPv6'


``elif``
========
* Used to check for additional condition if first is not met
* In other languages is known as ``else if``

.. code-block:: python

    language = 'Polish'

    if language == 'English':
        print('Hello')
    elif language == 'Russian':
        print('Здравствуйте')
    elif language == 'Germany':
        print('Guten tag!')
    elif language == 'Poland':
        print('Witaj!')
    else:
        print("I don't speak this language")

Switch statement
----------------
* No ``switch`` statement in Python!
* ``switch`` in Object Oriented Programming is considered a bad practise
* `PEP 275 <https://www.python.org/dev/peps/pep-0275/>`_

.. code-block:: python

    switch = {
        'English': 'Hello',
        'Russian': 'Здравствуйте',
        'German': 'Guten Tag',
        'Polish': 'Witaj',
    }


    language = 'French'

    switch.get(language, "I don't speak this language")
    # "I don't speak this language"

.. code-block:: python

    def switch(key):
        return {
            'English': 'Hello',
            'Russian': 'Здравствуйте',
            'German': 'Guten Tag',
            'Polish': 'Witaj',
        }.get(key, "I don't speak this language")

    switch('Russian')       # 'Здравствуйте'
    switch('French')        # "I don't speak this language"


Assignments
===========

Conditioning on user input
--------------------------
* Filename: ``control-flow/ifelse_input.py``
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min

#. Napisz program, który poprosi użytkownika o wiek
#. Użytkownik będzie podawał ``int`` lub ``float``, nie będzie próbował podawać niepoprawnych typów, np. ``str`` albo ``float`` z przecinkiem zamiast kropki
#. Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest "dorosła" czy "niepełnoletnia"

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie
    * Magic Number

``int`` and ``float``
---------------------
* Filename: ``control-flow/ifelse_integers.py``
* Lines of code to write: 7 lines
* Estimated time of completion: 10 min

#. Wczytaj liczbę od użytkownika (poda tylko ``int`` albo ``float``)
#. Wyświetl informację czy jest to liczba całkowita, czy niecałkowita.

:The whys and wherefores:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie

:Hints:
    * Liczba całkowita to taka, której część dziesiętna nie występuje lub jest równa zero.
    * Możesz to sprawdzić dzieląc liczbę z resztą przez *1* i sprawdzając resztę z dzielenia.
    * Zwróć uwagę, że ``input()`` zawsze zwraca ``str`` wiec trzeba rzutować na ``int``, ale wtedy tracimy informację czy wczesnej mieliśmy ``float``
