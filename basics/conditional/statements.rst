.. _Conditional Statements:

**********************
Conditional Statements
**********************


Positive and negative values
============================
.. highlights::
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


``if``
======
.. highlights::
    * The same indent level

Syntax
------
.. code-block:: python
    :caption: Single line statements

    if True:
        print('First line of the true statement')

.. code-block:: python
    :caption: Multiline blocks

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')
        print('Third line of the true statement')

Checking for simple value
-------------------------
.. code-block:: python

    age = 7

    if age == 7:
        print('Go to school')

.. code-block:: python
    :caption: Inside joke (see :ref:`José Jiménez`)

    job = 'astronaut'

    if job == 'astronaut':
        print('My name... José Jiménez')

.. code-block:: python

    number = 6

    if number % 2 == 0:
        print('Even')
    # Even

Checking if value is in range
-----------------------------
.. code-block:: python

    age = 7

    if 0 <= age < 18:
        print('Age is between [0, 18)')

Checking if has value
---------------------
.. highlights::
    * More advanced examples will be covered latter

.. code-block:: python

    name = input('What is your name?: ')
    # What is your name?: Jan Twardowski<Enter key>

    if name:
        print(f'My name is... {name}')
    # My name is Jan Twardowski

.. code-block:: python

    name = None

    if name:
        print(f'My name... {name}')


``else``
========
.. highlights::
    * Optional
    * Executed when condition is not met

Syntax
------
.. code-block:: python
    :caption: Single line statements

    if True:
        print('First line of the true statement')
    else:
        print('First line of the false statement')

.. code-block:: python
    :caption: Multiline blocks

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')
        print('Third line of the true statement')
    else:
        print('First line of the false statement')
        print('Second line of the false statement')
        print('Third line of the false statement')

Checking if variable is certain value
-------------------------------------
.. code-block:: python

    job = 'cosmonaut'

    if job == 'astronaut':
        print('NASA astronaut')
    else:
        print('Roscosmos cosmonaut')
    # Roscosmos cosmonaut

.. code-block:: python

    name = input('What is your name?: ')
    # What is your name?: <Enter key>

    if name:
        print(f'My name is... {name}')
    else:
        print('Did you forget to type your name?')
    # Did you forget to type your name?


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
.. highlights::
    * Used to check for additional condition if first is not met
    * In other languages is known as ``else if``

.. code-block:: python

    language = 'Polish'

    if language == 'English':
        print('Hello')
    elif language == 'Russian':
        print('Здравствуйте')
    elif language == 'German':
        print('Guten Tag')
    elif language == 'Polish':
        print('Witaj')
    else:
        print("I don't speak this language")

    # Witaj

Switch statement
----------------
.. highlights::
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
* Solution: :download:`solution/ifelse_input.py`

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
