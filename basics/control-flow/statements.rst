Conditional Statements
======================


Positive and Negative Values
----------------------------
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


Conditional Statement
---------------------
``if`` generic syntax:

.. code-block:: text

    if <condition>:
        <do something>

Single line statements:

    >>> if True:
    ...     print('First line of the true statement')
    First line of the true statement

Multiline blocks:

    >>> if True:
    ...     print('First line of the true statement')
    ...     print('Second line of the true statement')
    ...     print('Third line of the true statement')
    First line of the true statement
    Second line of the true statement
    Third line of the true statement

Multiline blocks:

    >>> if True:
    ...     print('First line of the true statement')
    ...     print('Second line of the true statement')
    ...
    ...     if True:
    ...         print('First line of inner true statement')
    First line of the true statement
    Second line of the true statement
    First line of inner true statement

Checking for simple value:

    >>> age = 7
    >>>
    >>> if age == 7:
    ...     print('Go to school')
    Go to school

Checking for simple value:

    >>> country = 'USA'
    >>>
    >>> if country == 'USA':
    ...     job = 'astronaut'
    >>>
    >>> print(job)
    astronaut

Checking for simple value:

    >>> number = 4
    >>>
    >>> if number % 2 == 0:
    ...     print('Even')
    Even

Checking if value is in range:

    >>> age = 7
    >>>
    >>> if 0 <= age < 18:
    ...     print('Age is between [0, 18)')
    Age is between [0, 18)

Checking if value is in range:

    >>> a = 10
    >>> b = 100
    >>>
    >>> if 0 <= a <= 50 < b:
    ...     print('Yes')
    Yes

Checking if has value:

    >>> input = lambda _: 'Jan Twardowski'  # Stub user input, for testing purpose only
    >>>
    >>> name = input('What is your name?: ')
    >>>
    >>> if name:
    ...     print(f'My name is... {name}')
    My name is... Jan Twardowski

Checking if has value:

    >>> input = lambda _: ''  # Stub user input, for testing purpose only
    >>>
    >>> name = input('What is your name?: ')
    >>>
    >>> if name:
    ...     print(f'My name... {name}')


Unconditional Alternative
-------------------------
* Optional
* Executed when condition is not met

``else`` generic syntax:

.. code-block:: text

    if <condition>:
        <do something>
    else:
        <do something>

Single line statements:

    >>> if True:
    ...     print('True statement')
    ... else:
    ...     print('Else statement')
    True statement

Multiline blocks:

    >>> if True:
    ...     print('True statement, first line')
    ...     print('True statement, second line')
    ... else:
    ...     print('Else statement, first line')
    ...     print('Else statement, second line')
    True statement, first line
    True statement, second line

Nested multiline blocks:

    >>> if True:
    ...     print('Outer block, true statement, first line')
    ...     print('Outer block, true statement, second line')
    ...
    ...     if True:
    ...         print('Inner block, true statement, first line')
    ...         print('Inner block, true statement, second line')
    ...     else:
    ...         print('Inner block, else statement, fist line')
    ...         print('Inner block, else statement, second line')
    ...
    ... else:
    ...     print('Outer block, else statement, first line')
    ...     print('Outer block, else statement, second line')
    Outer block, true statement, first line
    Outer block, true statement, second line
    Inner block, true statement, first line
    Inner block, true statement, second line

    >>> number = 3
    >>>
    >>> if number % 2 == 0:
    ...     print('Even')
    ... else:
    ...     print('Odd')
    Odd

Checking if variable is certain value:

    >>> country = 'Russia'
    >>>
    >>> if country == 'USA':
    ...     job = 'astronaut'
    ... else:
    ...     job = 'cosmonaut'
    >>>
    >>> print(job)
    cosmonaut

Checking if variable is certain value:

    >>> input = lambda _: ''  # Stub user input, for testing purpose only
    >>>
    >>> name = input('What is your name?: ')
    >>>
    >>> if name:
    ...     print(f'My name is... {name}')
    ... else:
    ...     print('Did you forget to type your name?')
    Did you forget to type your name?

    >>> data = [True, False, True]
    >>>
    >>> if any(data):
    ...     print('Yes')
    ... else:
    ...     print('No')
    Yes

    >>> data = [True, False, True]
    >>>
    >>> if all(data):
    ...     print('Yes')
    ... else:
    ...     print('No')
    No


Conditional Alternative
-----------------------
* Used to check for additional condition if first is not met
* In other languages is known as ``else if``

``elif`` generic syntax:

.. code-block:: text

    if <condition>:
        <do something>
    elif <condition>:
        <do something>
    else:
        <do something>

    >>> input = lambda _: 'Polish'  # Stub user input, for testing purpose only
    >>>
    >>> language = input('What is your language?: ')
    >>>
    >>> if language == 'English':
    ...     print('Hello')
    ... elif language == 'Russian':
    ...     print('Здравствуйте')
    ... elif language == 'German':
    ...     print('Guten Tag')
    ... elif language == 'Polish':
    ...     print('Witaj')
    ... else:
    ...     print("I don't speak this language")
    Witaj


Shorthand Expressions
---------------------
    >>> number = 3
    >>> is_even = (number % 2 == 0 )
    >>>
    >>> print(is_even)
    False

    >>> number = 3
    >>> is_digit = (number in range(0,10))
    >>>
    >>> print(is_digit)
    True


Conditional Expression
----------------------
    >>> number = 3
    >>>
    >>> if number in range(0,10):
    ...     is_digit = True
    ... else:
    ...     is_digit = False
    >>>
    >>> print(is_digit)
    True

    >>> number = 3
    >>> is_digit = True if number in range(0,10) else False
    >>>
    >>> print(is_digit)
    True

    >>> ip = '127.0.0.1'
    >>> protocol = 'IPv4' if '.' in ip else 'IPv6'
    >>>
    >>> print(protocol)
    IPv4

Normal ``if``:

    >>> country = 'Russia'
    >>>
    >>> if country == 'USA':
    ...     job = 'astronaut'
    ... else:
    ...     job = 'cosmonaut'
    >>>
    >>> print(job)
    cosmonaut

Inline ``if``:

    >>> country = 'Russia'
    >>> job = 'astronaut' if country == 'USA' else 'cosmonaut'
    >>>
    >>> print(job)
    cosmonaut

Type Str Methods is Numeric:

    >>> input = lambda _: '10'  # Stub user input, for testing purpose only
    >>>
    >>> age = input('What is your age?: ')
    >>> age = float(age) if age.isnumeric() else None
    >>> print(age)
    10.0


Switch
------
* No ``switch`` statement in Python!
* ``switch`` in Object Oriented Programming is considered a bad practise
* :pep:`275` -- Switching on Multiple Values [Rejected]

    >>> switch = {
    ...     'English': 'Hello',
    ...     'Russian': 'Здравствуйте',
    ...     'German': 'Guten Tag',
    ...     'Polish': 'Witaj',
    ...     'default': "I don't speak this language"}
    >>>
    >>> input = lambda _: 'French'  # Stub user input, for testing purpose only
    >>> language = input('What is your language?: ')
    >>>
    >>> switch.get(language, switch['default'])
    "I don't speak this language"

    >>> def switch(language):
    ...     data = {
    ...         'English': 'Hello',
    ...         'Russian': 'Здравствуйте',
    ...         'German': 'Guten Tag',
    ...         'Polish': 'Witaj',
    ...         'default': "I don't speak this language"}
    ...     return data.get(language, data['default'])
    >>>
    >>> switch('Russian')
    'Здравствуйте'
    >>>
    >>> switch('French')
    "I don't speak this language"


Pattern Matching
----------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial

    >>> # doctest: +SKIP
    ... def http_error(status):
    ...     match status:
    ...         case 400:
    ...             return 'Bad request'
    ...         case 401 | 403 | 405:
    ...             return 'Not allowed'
    ...         case 404:
    ...             return 'Not found'
    ...         case 418:
    ...             return "I'm a teapot"
    ...         case _:
    ...             return 'Unexpected status'

    >>> request = 'GET /index.html HTTP/2.0'
    >>>
    >>> # doctest: +SKIP
    ... match request.split():
    ...     case ['GET', uri, version]:
    ...         server.get(uri)
    ...     case ['POST', uri, version]:
    ...         server.post(uri)
    ...     case ['PUT', uri, version]:
    ...         server.put(uri)
    ...     case ['DELETE', uri, version]:
    ...         server.delete(uri)

    >>> # doctest: +SKIP
    ... match hero.action():
    ...    case ['move', ('up'|'down'|'left'|'right') as direction, value]:
    ...        hero.move(direction, value)
    ...    case ['make_damage', value]:
    ...        hero.make_damage(value)
    ...    case ['take_damage', value]:
    ...        hero.take_damage(value)

    >>> from enum import Enum
    >>>
    >>> class Key(Enum):
    ...     ESC = 27
    ...     ARROW_LEFT = 37
    ...     ARROW_UP = 38
    ...     ARROW_RIGHT = 39
    ...     ARROW_DOWN = 40
    >>>
    >>> # doctest: +SKIP
    ... match keyboard.on_key_press():
    ...     case Key.ESC:
    ...         game.quit()
    ...     case Key.ARROW_LEFT:
    ...         game.move_left()
    ...     case Key.ARROW_UP:
    ...         game.move_up()
    ...     case Key.ARROW_RIGHT:
    ...         game.move_right()
    ...     case Key.ARROW_DOWN:
    ...         game.move_down()
    ...     case _:
    ...         raise ValueError(f'Unrecognized key')

    >>> from enum import Enum
    >>>
    >>> class Color(Enum):
    ...     RED = 0
    ...     BLUE = 1
    ...     BLACK = 2
    >>>
    >>> # doctest: +SKIP
    ... match color:
    ...     case Color.RED:
    ...         print('Soviet')
    ...     case Color.BLUE:
    ...         print('Allies')
    ...     case Color.BLACK:
    ...         print('Axis')

    >>> from enum import Enum
    >>>
    >>> class SpaceMan(Enum):
    ...     NASA = 'Astronaut'
    ...     ESA = 'Astronaut'
    ...     ROSCOSMOS = 'Cosmonaut'
    ...     CNSA = 'Taikonaut'
    ...     ISRO = 'GaganYatri'
    >>>
    >>> # doctest: +SKIP
    ... match agency:
    ...     case SpaceMan.NASA:
    ...         print('USA')
    ...     case SpaceMan.ESA:
    ...         print('Europe')
    ...     case SpaceMan.ROSCOSMOS:
    ...         print('Russia')
    ...     case SpaceMan.CNSA:
    ...         print('China')
    ...     case SpaceMan.ISRO:
    ...         print('India')


Assignments
-----------
.. literalinclude:: assignments/controlflow_conditional_statements.py
    :caption: :download:`Solution <assignments/controlflow_conditional_statements.py>`
    :end-before: # Solution
