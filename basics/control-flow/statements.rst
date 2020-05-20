.. _Conditional Statements:

**********************
Conditional Statements
**********************


Positive and negative values
============================
.. highlights::
    Negative values:

        * empty ``bool()`` or ``False``
        * empty ``int()`` or ``0``
        * empty ``float()`` or ``0.0``
        * empty ``complex()`` or ``0+0j`` or ``0.0+0.0j``
        * empty ``str()`` or ``''``
        * empty ``tuple()`` or ``()``
        * empty ``list()`` or ``[]``
        * empty ``set()``
        * empty ``frozenset()``
        * empty ``dict()`` or ``{}``
        * ``None``

    Positive values:

        * any other


``if``
======
.. code-block:: python
    :caption: ``if`` generic syntax
    :force:

    if <condition>:
        <do something>

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

.. code-block:: python
    :caption: Checking for simple value

    age = 7

    if age == 7:
        print('Go to school')

.. code-block:: python
    :caption: Checking for simple value.

    country = 'USA'

    if country == 'USA':
        print('Astronauts are from USA')

.. code-block:: python
    :caption: Checking for simple value

    number = 6

    if number % 2 == 0:
        print('Even')
    # Even

.. code-block:: python
    :caption: Checking if value is in range

    age = 7

    if 0 <= age < 18:
        print('Age is between [0, 18)')
    # Age is between [0, 18)

.. code-block:: python
    :caption: Checking if value is in range

    a = 10
    b = 100

    if 0 <= a <= 50 < b:
        print('Yes')
    # Yes

.. code-block:: python
    :caption: Checking if has value

    name = input('What is your name?: ')
    # What is your name?: Jan Twardowski<ENTER>

    if name:
        print(f'My name is... {name}')
    # My name is Jan Twardowski

.. code-block:: python
    :caption: Checking if has value

    name = input('What is your name?: ')
    # What is your name?: <ENTER>

    if name:
        print(f'My name... {name}')


``else``
========
.. highlights::
    * Optional
    * Executed when condition is not met

.. code-block:: python
    :caption: ``else`` generic syntax
    :force:

    if <condition>:
        <do something>
    else:
        <do something>

.. code-block:: python
    :caption: Single line statements

    if True:
        print('True statement')
    else:
        print('Else statement')

.. code-block:: python
    :caption: Multiline blocks

    if True:
        print('True statement, first line')
        print('True statement, second line')
    else:
        print('Else statement, first line')
        print('Else statement, second line')

.. code-block:: python
    :caption: Nested multiline blocks

    if True:
        print('Outer block, true statement, first line')
        print('Outer block, true statement, second line')

        if True:
            print('Inner block, true statement, first line')
            print('Inner block, true statement, second line')
        else:
            print('Inner block, else statement, fist line')
            print('Inner block, else statement, second line')

    else:
        print('Outer block, else statement, first line')
        print('Outer block, else statement, second line')

.. code-block:: python
    :caption: Checking if variable is certain value

    country = 'Russia'

    if country == 'USA':
        print('Astronauts are from USA')
    else:
        print('Cosmonauts are from Russia')
    # Cosmonauts are from Russia

.. code-block:: python
    :caption: Checking if variable is certain value

    name = input('What is your name?: ')
    # What is your name?: <ENTER>

    if name:
        print(f'My name is... {name}')
    else:
        print('Did you forget to type your name?')
    # Did you forget to type your name?

.. code-block:: python

    data = [True, False, True]

    if any(data):
        print('Yes')
    else:
        print('No')

    # Yes

.. code-block:: python

    data = [True, False, True]

    if all(data):
        print('Yes')
    else:
        print('No')

    # No


Inline If
=========
.. code-block:: python
    :caption: Normal ``if``

    country = 'Russia'

    if country == 'Russia':
        job = 'cosmonaut'
    else:
        job = 'astronaut'

.. code-block:: python
    :caption: Inline ``if``

    country = 'Russia'

    job = 'cosmonaut' if country == 'Russia' else 'astronaut'


Elif
====
.. highlights::
    * Used to check for additional condition if first is not met
    * In other languages is known as ``else if``

.. code-block:: python
    :caption: ``elif`` generic syntax
    :force:

    if <condition>:
        <do something>
    elif <condition>:
        <do something>
    else:
        <do something>

.. code-block:: python

    language = input('What is your name?: ')
    # What is your name?: Polish<ENTER>

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


Switch
======
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
        'default': "I don't speak this language"}


    language = input('What is your name?: ')
    # What is your name?: French<ENTER>

    switch.get(language, switch['default'])
    # "I don't speak this language"

.. code-block:: python

    def switch(key):
        data = {
            'English': 'Hello',
            'Russian': 'Здравствуйте',
            'German': 'Guten Tag',
            'Polish': 'Witaj',
            'default': "I don't speak this language"}
        return data.get(language, data['default'])


    switch('Russian')       # 'Здравствуйте'
    switch('French')        # "I don't speak this language"


Assignments
===========

Conditioning on user input
--------------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/conditional_ifelse.py`

:English:
    #. Ask user to input age
    #. User will pass only valid ``int``
    #. Print whether user is adult

:Polish:
    #. Poproś użytkownika o wprowadzenie swojego wieku
    #. Użytkownika poda tylko poprawne ``int``
    #. Wypisz czy użytkownik jest pełnoletni

:The whys and wherefores:
    * Reading input
    * Type casting
    * Conditional statements
    * Defining variables
    * Magic Number
