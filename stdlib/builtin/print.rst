.. _Builtin Printing:

****************
Builtin Printing
****************


``print`` function
==================

Function definition
-------------------
.. code-block:: python

    def print(*values, sep=' ', end='\n', file=sys.stdout, flush=False):
        """
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
        """
        ...

Intuitive implementation
------------------------
.. code-block:: python
    :caption: Intuitive implementation of ``print`` function

    def print(*values, sep=' ', end='\n', ...):
        return sep.join(values) + end

Printing multiple values
------------------------
.. code-block:: python

    name = 'José Jiménez'

    print('My name...', name, '!')
    # My name... José Jiménez!

.. code-block:: python

    name = 'José Jiménez'

    print('My name...', name, '!', sep=';')
    # My name...;José Jiménez;!


String concatenation
====================
* ``+`` operator (with side effects)
* ``str.join()``
* ``str.format()``
* f-string formatting (preferred)

``+`` Operator
--------------
* f-string formatting are preferred over ``str`` addition
* How many ``str`` are in the memory?

.. code-block:: python

    name = 'José Jiménez'

    'My name... ' + name
    # 'My name... José Jiménez'

.. code-block:: python
    :caption: ``+`` Operator side effect

    name = 'José Jiménez'
    age = 42

    'My name... ' + name + ' and I am ' + str(age) + ' years old!'
    # 'My name... José Jiménez and I am 42 years old!'

``str.join()``
--------------
.. code-block:: python

    data = ['Jan Twardowski', 'Mark Watney', 'José Jiménez']

    ' '.join(data)              # 'Jan Twardowski Mark Watney José Jiménez'
    ','.join(data)              # 'Jan Twardowski,Mark Watney,José Jiménez'
    ', '.join(data)             # 'Jan Twardowski, Mark Watney, José Jiménez'


Variable interpolation
======================

Operator: ``%s``, ``%d``, ``%f``
--------------------------------
* positional
* keyword
* ``%s`` - ``str``
* ``%d`` - ``int``
* ``%f`` - ``float``

.. code-block:: python

    name = 'José Jiménez'
    age = 42
    pi = 3.141592653589793

    'My name... %s' % name             # My name... José Jiménez
    'My name... %d' % name             # TypeError: %d format: a number is required, not str
    'My name... %f' % name             # TypeError: must be real number, not str

    'I have %s years' % age             # 'I have 42 years'
    'I have %d years' % age             # 'I have 42 years'
    'I have %f years' % age             # 'I have 42.000000 years'

    'Number PI is %s' % pi              # 'Number PI is 3.141592653589793'
    'Number PI is %f' % pi              # 'Number PI is 3.141593'
    'Number PI is %d' % pi              # 'Number PI is 3'

.. code-block:: python

    name = 'José Jiménez'
    age = 42

    '%s has %s years' % (name, age))      # José Jiménez has 42 years
    '%s has %s years' % (age, name))      # 42 has José Jiménez years

.. code-block:: python

    pi = 3.141592653589793

    def square(value):
        return value ** 2

    'PI squared is %f' % square(pi)      # 'PI squared is 9.869604'

.. code-block:: python

    data = {
        'name': 'José Jiménez',
        'age': 42,
    }

    '%(name)s has %(age)d years' % data
    # 'José Jiménez has 42 years'

    '%(name)s has %(age)d years' % {'name': 'José Jiménez', 'age': 42}
    # 'José Jiménez has 42 years'

.. code-block:: python

    name = 'José Jiménez'
    age = 42

    'My name... %(name)s' % locals()
    # 'My name... José Jiménez'

``str.format()``
----------------
.. code-block:: python

    name = 'José Jiménez'
    age = 42

    '{} is {} years'.format(name, age)                     # 'José Jiménez is 42 years'
    '{0} is {1} years'.format(name, age)                   # 'José Jiménez is 42 years'
    '{1} is {0} years'.format(name, age)                   # '42 is José Jiménez years'

.. code-block:: python

    name = 'José Jiménez'
    age = 42

    '{a} is {b} years'.format(a=name, b=age)               # 'José Jiménez is 42 years'
    '{name} is {age} years'.format(name=name, age=age)     # 'José Jiménez is 42 years'
    '{age} is {name} years'.format(**locals())             # '42 is José Jiménez years'

f-strings - Python >= 3.6
-------------------------
* Preferred way

.. code-block:: python

    name = 'José Jiménez'
    pi = 3.141592653589793

    def square(value):
        return value ** 2

    f'My name... {name}'                      # 'My name... José Jiménez'
    f'PI squared is {square(pi)}'             # 'PI squared is 9.869604401089358'

.. code-block:: python

    from datetime import datetime


    now = datetime.now()
    iso = '%Y-%m-%dT%H:%M:%SZ'

    f'Today is: {now:%Y-%m-%d}')              # 'Today is: 1969-07-21'
    f'Today is: {now:{iso}}')                 # 'Today is: 1969-07-21T02:56:15Z'


Advanced String Formatting
==========================
* :pep:`3101`

Basic formatting
----------------
.. code-block:: python

    text = 'PI'
    number = 3.14

    f'{text} = {number}'            # 'PI = 3.14'

Padding and aligning strings
----------------------------
.. code-block:: python

    text = 'hello'

    f'{text:10}'                    # 'hello     '
    f'{text:<10}'                   # 'hello     '
    f'{text:^10}'                   # '  hello   '
    f'{text:>10}'                   # '     hello'
    f'{text:.<10}'                  # 'hello.....'
    f'{text:_^10}'                  # '__hello___'

Type casting
------------
.. code-block:: python

    number = 3

    f'{number}'                    # '3'
    f'{number:d}'                  # '3'
    f'{number:f}'                  # '3.000000'

.. code-block:: python

    number = 3.141592653589793

    f'{number}'                     # '3.141592653589793'
    f'{number:d}'                   # ValueError: Unknown format code 'd' for object of type 'float'
    f'{number:f}'                   # '3.141593'

.. code-block:: python

    text = 'hello'

    f'{text}'                       # 'hello'
    f'{text:d}'                     # ValueError: Unknown format code 'd' for object of type 'str'
    f'{text:f}'                     # ValueError: Unknown format code 'f' for object of type 'str'

.. code-block:: python

    f'{14:#b}'                      # '0b1110'
    f'{14:b}'                       # '1110'

.. code-block:: python

    f'{10:#o}'                      # '0o12'
    f'{10:o}'                       # '12'

.. code-block:: python

    f'{255:#x}'                     # '0xff'
    f'{255:x}'                      # 'ff'
    f'{255:X}'                      # 'FF'

Truncating and rounding
-----------------------
.. code-block:: python

    text = 'Lorem Ipsum'

    f'{text:.5}'                    # 'Lorem'
    f'{text:10.5}'                  # 'Lorem     '

.. code-block:: python

    number = 3.141592653589793

    f'{number:.2f}'                 # '3.14'
    f'{number: 6.2f}'               # '  3.14'
    f'{number:06.2f}'               # '003.14'
    f'{number:.6.2f}'               # ValueError: Invalid format specifier

Signed numbers
--------------
.. code-block:: python

    positive = 42
    negative = -42


    f'{positive:d}'                 # '42'
    f'{negative:d}'                 # '-42'

    f'{positive: d}'                # ' 42'
    f'{negative: d}'                # '-42'

    f'{positive:+d}'                # '+42'
    f'{negative:+d}'                # '-42'

    f'{negative:=5d}'               # '-  42'
    f'{positive:=+5d}'              # '+  42'

Get from ``dict``
-----------------
.. code-block:: python

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski'
    }

    f'{data["first_name"]}'         # 'Jan'
    f'{data["last_name"]}'          # 'Twardowski'

Get from ``sequence``
---------------------
.. code-block:: python

    data = ['a', 'b', 'c']

    f'{data[1]}'                    # 'b'
    f'{data[0]} -> {data[2]}'       # 'a -> c'

.. code-block:: python

    data = ('a', 'b', 'c')

    f'{data[1]}'                    # 'b'
    f'{data[0]} -> {data[2]}'       # 'a -> c'

.. code-block:: python

    data = {'a', 'b', 'c'}

    f'{data[1]}'
    # TypeError: 'set' object is not subscriptable

Get from ``class``
------------------
.. code-block:: python

    class Iris:
        species = 'setosa'
        measurements = {
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.3,
            'petal_width': 0.4,
        }

    flower = Iris()

    f'{flower.species}'                             # 'setosa'
    f'{flower.species:.3}'                          # 'set'
    f'{flower.measurements["sepal_width"]}'         # '3.5'
    f'{flower.measurements["sepal_width"]:.3f}'     # '3.500'

Parametrized formats
--------------------
.. code-block:: python

    text = 'hello'

    align = '^'
    width = 10


    f'{text:{align}}'               # 'hello'
    f'{text:{align}{width}}'        # '  hello   '

.. code-block:: python

    number = 3.14159

    align = '>'
    width = 10
    precision = 2
    sign = '+'


    f'{number:.{precision}f}'                       # '3.14'
    f'{number:{width}.{precision}f}'                # '      3.14'
    f'{number:{align}{sign}{width}.{precision}f}'   # '     +3.14'

Datetime
--------
.. code-block:: python

    from datetime import datetime


    now = datetime(1969, 7, 21, 2, 56, 15)

    iso = '%Y-%m-%dT%H:%M:%SZ'
    date = '%Y-%m-%d'
    time = '%H:%M'


    f'{now:%Y-%m-%d %H:%M}'       # '1969-07-21 02:56'

    f'{now:{iso}}'                # '1969-07-21T02:56:15Z'
    f'{now:{date}}'               # '1969-07-21'
    f'{now:{time}}'               # '02:56'

Custom object formatting
------------------------
.. code-block:: python

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z

        def __format__(self, format):

            if format == '2D':
                return f"({self.x}, {self.y})"

            elif format == '3D':
                return f"({self.x}, {self.y}, {self.z})"

            elif format == 'dict':
                return str(self.__dict__)

            elif format == 'tuple':
                return str(tuple(self.__dict__.values()))

            elif format == 'json':
                import json
                return json.dumps(self.__dict__)

            else:
                raise ValueError


    point = Point(x=1, y=2)

    f'{point:2D}'           # '(1, 2)'
    f'{point:3D}'           # '(1, 2, 0)'
    f'{point:tuple}'        # '(1, 2, 0)'
    f'{point:dict}'         # "{'x': 1, 'y': 2, 'z': 0}"
    f'{point:json}'         # '{"x": 1, "y": 2, "z": 0}'

``str`` and ``repr``
--------------------
* ``!s`` executes ``__str__()``
* ``!r`` executes ``__repr__()``

.. code-block:: python

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z

        def __str__(self):
            return f'({self.x}, {self.y}, {self.z})'

        def __repr__(self):
            return f'Point(x={self.x}, y={self.y}, z={self.z})'


    point = Point(x=1, y=2)

    f'{point!s}'            # '(1, 2, 0)'
    f'{point!r}'            # 'Point(x=1, y=2, z=0)'

Quick and easy debugging
------------------------
.. versionadded:: Python 3.8
    See https://bugs.python.org/issue36817

* ``f'{expr=}'`` expands to the text of the expression, an equal sign, then the repr of the evaluated expression

.. code-block:: python

    number = 3

    f'{number*9 + 15=}'
    # x*9 + 15=42

.. code-block:: python

    user = 'eric_idle'
    member_since = date(1975, 7, 31)

    f'{user=} {member_since=}'
    # "user='eric_idle' member_since=datetime.date(1975, 7, 31)"

.. code-block:: python

    delta = date.today() - member_since

    f'{user=!s}  {delta.days=:,d}'
    # 'user=eric_idle  delta.days=16,075'

.. code-block:: python

    print(f'{theta=}  {cos(radians(theta))=:.3f}')
    # theta=30  cos(radians(theta))=0.866

``pprint``
==========
.. code-block:: python

    from pprint import pprint

    data = [{'first_name': 'José', 'last_name': 'Jiménez'}, {'first_name': 'Mark', 'last_name': 'Watney'}, {'first_name': 'Иван', 'last_name': 'Иванович'}]

    pprint(data)
    # [{'first_name': 'José', 'last_name': 'Jiménez'},
    #  {'first_name': 'Mark', 'last_name': 'Watney'},
    #  {'first_name': 'Иван', 'last_name': 'Иванович'}]

.. code-block:: python

    from pprint import pformat

    data = [{'first_name': 'José', 'last_name': 'Jiménez'}, {'first_name': 'Mark', 'last_name': 'Watney'}, {'first_name': 'Иван', 'last_name': 'Иванович'}]

    # returns formatted data
    my_string = pformat(data)


Assignments
===========

Powielanie napisów
------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/print_lines.py`

:English:
    .. todo:: English translation

:Polish:
    #. Dany jest ciąg znaków: ``text = 'Lorem Ipsum'``
    #. Napisz trzy funkcje:

        * ``print_1(text)`` wykorzystującą ``range()``
        * ``print_2(text)`` wykorzystującą pętlę ``while``
        * ``print_3(text)`` wykorzystującą mnożenie stringów

    #. Każda funkcja ma wyświetlić 5 kopii tego ciągu znaków
    #. Każdy ciąg znaków w osobnej linii
    #. Napisz doctest do wszystkich funkcji

:The whys and wherefores:
    * wczytywanie ciągu znaków od użytkownika
    * formatowanie ciągu znaków
    * korzystanie z pętli i instrukcji warunkowych

Przeliczanie temperatury
------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/print_formatting.py`

:English:
    .. todo:: English translation

:Polish:
    #. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni).
    #. Wynik musi być taki jak na listingu poniżej
    #. Znak ma być zawsze wyświetlany
    #. Zwróć uwagę na wyjustowanie tekstu
    #. Zwróć uwagę na wypełnienie miejsca niezajętego przez cyfry

:Output:
    .. code-block:: text

        -------------------------------------------
        | Temperature | -     20°C | ....-4....°F |
        -------------------------------------------
        | Temperature | -     15°C | ....+5....°F |
        -------------------------------------------
        | Temperature | -     10°C | ...+14....°F |
        -------------------------------------------
        | Temperature | -      5°C | ...+23....°F |
        -------------------------------------------
        | Temperature | +      0°C | ...+32....°F |
        -------------------------------------------
        | Temperature | +      5°C | ...+41....°F |
        -------------------------------------------
        | Temperature | +     10°C | ...+50....°F |
        -------------------------------------------
        | Temperature | +     15°C | ...+59....°F |
        -------------------------------------------
        | Temperature | +     20°C | ...+68....°F |
        -------------------------------------------
        | Temperature | +     25°C | ...+77....°F |
        -------------------------------------------
        | Temperature | +     30°C | ...+86....°F |
        -------------------------------------------
        | Temperature | +     35°C | ...+95....°F |
        -------------------------------------------
        | Temperature | +     40°C | ...+104...°F |

:Hints:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * .. code-block:: python

        def celsius_to_fahrenheit(degree):
            return degree*1.8 + 32

:The whys and wherefores:
    * zaawansowane formatowanie ciągu znaków
