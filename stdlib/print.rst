.. _Print Formatting:

****************
Print Formatting
****************

Python umożliwia kilka sposobów manipulacji stringami i uwzględnianie zmiennych w wyświetlanych napisach.

Funkcja ``print``
=================
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

Konkatenacja stringów
=====================
* Wykorzystanie parametrów funkcji ``print()``
* Operator ``+`` (with side effects)
* ``str.join()``
* ``str.format()``
* f-string formatting (preferred)

Wykorzystanie parametrów funkcji ``print()``
--------------------------------------------
.. code-block:: python

    name = 'José Jiménez'

    print('My name...', name, '!')
    # My name... José Jiménez!

.. code-block:: python

    name = 'José Jiménez'

    print('My name...', name, '!', sep=';')
    # My name...;José;Jiménez!

Operator ``+``
--------------
.. code-block:: python

    name = 'José Jiménez'

    'My name... ' + name + '!'
    # My name... José Jiménez!

.. code-block:: python

    name = 'José Jiménez'
    age = 42

    print('My name... ' + name + ' and I am ' + str(age) + ' years old!')
    # My name... José Jiménez and I am 42 years old!

Operator ``+`` side effect
--------------------------
* f-string formatting are preferred over ``str`` addition
* How many ``str`` are in the memory?

.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'


    first_name + ' ' + last_name
    # José Jiménez

.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    f'{first_name} {last_name}'
    # José Jiménez

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

    def my(name):
        return name

    print('My name... %s!' % name)              # My name... José Jiménez!
    print("%s has %s years" % (name, age))      # José Jiménez has 42 years
    print('%s has %s years' % (age, name))      # 42 has José Jiménez years
    print('%s has %.1f years' % (name, age))    # José Jiménez has 42.0 years
    print('%s has %10.1f years' % (name, age))  # José Jiménez has       42.0 years
    print('%s has %d years' % (my(name), age))  # José Jiménez has 42 years

    print('%(name)s has %(age)d years' % {
        'age': age,
        'name': name,
    })
    # José Jiménez has 42 years

    print('My name... %(name)s.' % locals())
    # My name... José Jiménez.


Metoda ``.format()``
--------------------
.. code-block:: python

    name = 'José Jiménez'
    age = 42

    print('{name} is {age} years'.format(name=name, age=age))   # 'José Jiménez is 42 years'
    print('{age} is {name} years'.format(**locals()))           # '42 is José Jiménez years'
    print('{} is {} years'.format(name, age))                   # 'José Jiménez is 42 years'
    print('{0} is {1} years'.format(name, age))                 # 'José Jiménez is 42 years'
    print('{1} is {0} years'.format(name, age))                 # '42 is José Jiménez years'
    print('{1:.3} is {0:.1} years'.format(float(age), name))    # 'Jos is 42.0 years'
    print('{1:.3} is {0:10.1} years'.format(float(age), name))  # 'Jos is       42.0 years'


f-strings - Python >= 3.6
-------------------------
* ``f'{variable}'``
* ``f'{self.field}'``
* ``f'{datetime:%Y-%m-%d %H:%M}'``

.. code-block:: python

    import datetime

    name = 'José'
    age = 42
    now = datetime.datetime.utcnow()
    format = '%Y-%m-%d %H:%M:%S'

    def my(name):
        return name

    print(f'My name... {name}!')                                     # 'My name... José Jiménez'
    print(f'My name... {my(name)}, age: {age} years')                # 'My name... José, age: 42 years'
    print(f'Today is: {now:%Y-%m-%d %H:%M:%S}')                      # 'Today is: 1969-07-21 02:56:15'
    print(f'Today is: {now:{format}}')                               # 'Today is: 1969-07-21 02:56:15'


PEP 3101 -- Advanced String Formatting
======================================
* https://www.python.org/dev/peps/pep-3101/

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

    f'{number}'                   # '3.141592653589793'
    f'{number:d}'                 # ValueError: Unknown format code 'd' for object of type 'float'
    f'{number:f}'                 # '3.141593'

.. code-block:: python

    text = 'hello'

    f'{text}'                     # 'hello'
    f'{text:d}'                   # ValueError: Unknown format code 'd' for object of type 'str'
    f'{text:f}'                   # ValueError: Unknown format code 'f' for object of type 'str'

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

    f'{data["first_name"]}'       # 'Jan'
    f'{data["last_name"]}'        # 'Twardowski'

Get from ``sequence``
---------------------
.. code-block:: python

    data = ['a', 'b', 'c']

    f'{data[1]}'                  # 'b'
    f'{data[0]} -> {data[2]}'     # 'a -> c'

.. code-block:: python

    data = ('a', 'b', 'c')

    f'{data[1]}'                  # 'b'
    f'{data[0]} -> {data[2]}'     # 'a -> c'

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


    f'{text:{align}}'           # 'hello'
    f'{text:{align}{width}}'    # '  hello   '

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


    now = datetime(1969, 7, 21, 14, 56, 15)

    iso = '%Y-%m-%dT%H:%M:%SZ'
    date = '%Y-%m-%d'
    time = '%H:%M'


    f'{now:%Y-%m-%d %H:%M}'       # '1969-07-21 14:56'

    f'{now:{iso}}'                # '1969-07-21T14:56:15Z'
    f'{now:{date}}'               # '1969-07-21'
    f'{now:{time}}'               # '14:56'

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

    f'{point:2D}'       # '(1, 2)'
    f'{point:3D}'       # '(1, 2, 0)'
    f'{point:tuple}'    # '(1, 2, 0)'
    f'{point:dict}'     # "{'x': 1, 'y': 2, 'z': 0}"
    f'{point:json}'     # '{"x": 1, "y": 2, "z": 0}'

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

    f'{point!s}'    # '(1, 2, 0)'
    f'{point!r}'    # 'Point(x=1, y=2, z=0)'

Quick and easy debugging
------------------------
* since Python 3.8
* ``f'{expr=}'`` expands to the text of the expression, an equal sign, then the repr of the evaluated expression

.. code-block:: python

    number = 3

    f'{number*9 + 15=}'
    # x*9 + 15=42


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
* Filename: :download:`solution/print_lines.py`
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min

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
* Filename: :download:`solution/print_formatting.py`
* Lines of code to write: 8 lines
* Estimated time of completion: 15 min

#. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni).
#. Wynik musi być taki jak na listingu poniżej
#. Znak ma być zawsze wyświetlany
#. Zwróć uwagę na wyjustowanie tekstu
#. Zwróć uwagę na wypełnienie miejsca niezajętego przez cyfry

    .. code-block:: text

        -------------------------------------------
        | Temperatura | -     20°C | ....-4....°F |
        -------------------------------------------
        | Temperatura | -     15°C | ....+5....°F |
        -------------------------------------------
        | Temperatura | -     10°C | ...+14....°F |
        -------------------------------------------
        | Temperatura | -      5°C | ...+23....°F |
        -------------------------------------------
        | Temperatura | +      0°C | ...+32....°F |
        -------------------------------------------
        | Temperatura | +      5°C | ...+41....°F |
        -------------------------------------------
        | Temperatura | +     10°C | ...+50....°F |
        -------------------------------------------
        | Temperatura | +     15°C | ...+59....°F |
        -------------------------------------------
        | Temperatura | +     20°C | ...+68....°F |
        -------------------------------------------
        | Temperatura | +     25°C | ...+77....°F |
        -------------------------------------------
        | Temperatura | +     30°C | ...+86....°F |
        -------------------------------------------
        | Temperatura | +     35°C | ...+95....°F |
        -------------------------------------------
        | Temperatura | +     40°C | ...+104...°F |

:Hints:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * .. code-block:: python

        def celsius_to_fahrenheit(degree):
            return degree*1.8 + 32

:The whys and wherefores:
    * zaawansowane formatowanie ciągu znaków
