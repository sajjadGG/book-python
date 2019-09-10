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
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/ifelse_input.py`

:English:
    #. Ask user for age
    #. User will pass only valid ``int``
    #. Print whether user is adult

:Polish:
    #. Poproś użytkownika o wiek
    #. Użytkownika poda tylko poprawne ``int``
    #. Wypisz czy użytkownik jest pełnoletni

:The whys and wherefores:
    * Reading input
    * Type casting
    * Conditional statements
    * Defining variables
    * Magic Number

Is odd number
-------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/ifelse_is_odd.py`

:English:
    #. Read a number from user
    #. User will pass only valid ``int``
    #. Print whether number is odd
    #. Number is odd, when divided modulo (``%``) by 2 has a reminder

:Polish:
    #. Wczytaj liczbę od użytkownika
    #. Użytkownika poda tylko poprawne ``int``
    #. Wypisz czy liczba jest nieparzysta
    #. Liczba jest nieparzysta, gdy dzielona modulo (``%``) przez 2 ma resztę

:The whys and wherefores:
    * Reading input from user
    * Type casting
    * Print formatting
    * Numerical operators

:Hints:
    * ``%`` has different meaning for ``int`` and ``str``
