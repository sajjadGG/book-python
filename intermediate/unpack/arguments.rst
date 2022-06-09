Unpack Arguments
================
* Unpack and Arbitrary Number of Parameters and Arguments

.. figure:: img/unpack-assignment,args,params.png



Recap
-----
* Argument - Value or variable being passed to the function
* Positional arguments - value passed to function
* Positional arguments - order is important
* Positional arguments - must be at the left side
* Keyword arguments - value passed to function resolved by name
* Keyword arguments - order is not important
* Keyword arguments - must be on the right side
* Positional argument cannot follow keyword arguments

>>> def echo(a=None, b=None):
...     ...

>>> echo(1)          # positional argument
>>> echo(a=1)        # keyword argument
>>> echo(1, 2)       # positional arguments
>>> echo(2, 1)       # positional arguments
>>> echo(a=1, b=2)   # keyword arguments
>>> echo(b=2, a=1)   # keyword arguments, order doesn't matter
>>> echo(1, b=2)     # positional and keyword arguments

>>> echo(a=1, 2)
Traceback (most recent call last):
SyntaxError: positional argument follows keyword argument


Positional Arguments
--------------------
* ``*`` is used for positional arguments
* there is no convention, but you can use any name
* ``*`` unpacks from ``tuple``, ``list`` or ``set``

>>> def echo(a, b, c):
...     print(f'{a=}, {b=}, {c=}')
>>>
>>>
>>> echo(1, 2, 3)
a=1, b=2, c=3
>>>
>>> data = (1, 2, 3)
>>> echo(data)
Traceback (most recent call last):
TypeError: echo() missing 2 required positional arguments: 'b' and 'c'
>>>
>>> data = (1, 2, 3)
>>> echo(data[0], data[1], data[2])
a=1, b=2, c=3
>>>
>>> data = (1, 2, 3)
>>> echo(*data)
a=1, b=2, c=3


Keyword Arguments
-----------------
* ``**`` is used for keyword arguments
* there is no convention, but you can use any name
* ``**`` unpacks from ``dict``

Keyword arguments passed directly:

>>> def echo(a, b, c):
...     print(f'{a=}, {b=}, {c=}')
>>>
>>>
>>> echo(a=1, b=2, c=3)
a=1, b=2, c=3
>>>
>>> data = {'a': 1, 'b': 2, 'c': 3}
>>> echo(a=data['a'], b=data['b'], c=data['c'])
a=1, b=2, c=3
>>>
>>> data = {'a': 1, 'b': 2, 'c': 3}
>>> echo(**data)
a=1, b=2, c=3


Positional and Keyword Arguments
--------------------------------
>>> def echo(a, b, c, d):
...     print(f'{a=}, {b=}, {c=}, {d=}')

>>> echo(1, 2, c=3, d=4)
a=1, b=2, c=3, d=4

>>> data1 = (1, 2)
>>> data2 = {'c': 3, 'd': 4}
>>> echo(data1[0], data1[1], c=data2['c'], d=data2['d'])
a=1, b=2, c=3, d=4

>>> data1 = (1, 2)
>>> data2 = {'c': 3, 'd': 4}
>>> echo(*data1, **data2)
a=1, b=2, c=3, d=4

>>> data1 = (1, 2)
>>> data2 = {'c': 3}
>>> echo(*data1, **data2)
Traceback (most recent call last):
TypeError: echo() missing 1 required positional argument: 'd'

>>> data1 = (1, 2)
>>> data2 = {'c': 3, 'd': 4, 'a': 1}
>>> echo(*data1, **data2)
Traceback (most recent call last):
TypeError: echo() got multiple values for argument 'a'


Objects From Sequence
---------------------
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
>>>
>>>
>>> DATA = (6.0, 3.4, 4.5, 1.6, 'versicolor')
>>>
>>> result = Iris(*DATA)
>>>
>>> vars(result)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 6.0,
 'sepal_width': 3.4,
 'petal_length': 4.5,
 'petal_width': 1.6,
 'species': 'versicolor'}

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
...
...     def __repr__(self):
...         return str(vars(self))
>>>
>>>
>>> result = [Iris(*row) for row in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'},
 {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
 {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
 {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
 {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'},
 {'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.3, 'petal_width': 0.2, 'species': 'setosa'}]


Objects From Mappings
---------------------
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
>>>
>>>
>>> DATA = {"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_width":1.9,"species":"virginica"}
>>>
>>> iris = Iris(**DATA)
>>>
>>> vars(iris)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}

>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
...
...     def __repr__(self):
...         return str(vars(self))
>>>
>>>
>>> DATA = [{"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_width":1.9,"species":"virginica"},
...         {"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2,"species":"setosa"},
...         {"sepal_length":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"species":"versicolor"},
...         {"sepal_length":6.3,"sepal_width":2.9,"petal_length":5.6,"petal_width":1.8,"species":"virginica"},
...         {"sepal_length":6.4,"sepal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versicolor"},
...         {"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"petal_width":0.2,"species":"setosa"}]
>>>
>>> result = [Iris(**row) for row in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'},
 {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
 {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
 {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
 {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'},
 {'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.3, 'petal_width': 0.2, 'species': 'setosa'}]


Use Case - 0x01
---------------
Calling a function which has similar parameters. Passing configuration to the
function, which sets parameters from the config:

>>> def draw_line(x, y, color, type, width, markers):
...     pass

>>> draw_line(x=1, y=2, color='red', type='dashed', width='2px', markers='disc')
>>> draw_line(x=3, y=4, color='red', type='dashed', width='2px', markers='disc')
>>> draw_line(x=5, y=6, color='red', type='dashed', width='2px', markers='disc')

>>> style = {'color': 'red',
...          'type': 'dashed',
...          'width': '2px',
...          'markers': 'disc'}
>>>
>>> draw_line(x=1, y=2, **style)
>>> draw_line(x=3, y=4, **style)
>>> draw_line(x=5, y=6, **style)


Use Case - 0x02
---------------
>>> def print_coordinates(x, y, z):
...     print(f'{x=}, {y=}, {z=}')

Passing sequence to the function:

>>> point_xyz = [1, 2, 3]
>>>
>>> print_coordinates(point_xyz[0], point_xyz[1], point_xyz[2])
>>> print_coordinates(*point_xyz)

Passing mapping to the function:

>>> point_xyz = {'x': 1, 'y': 2, 'z': 3}
>>>
>>> print_coordinates(x=point_xyz['x'], y=point_xyz['y'], z=point_xyz['z'])
>>> print_coordinates(**point_xyz)
>>> print_coordinates(*point_xyz.values())

Passing sequence and mapping to the function:

>>> point_xy = (1, 2)
>>> point_z = {'z': 3}
>>> print_coordinates(*point_xy, **point_z)


Use Case - 0x03
---------------

>>> def database_connect(host, port, username, password, database):
...     pass
>>>
>>>
>>> CONFIG = {
...     'host': 'example.com',
...     'port': 5432,
...     'username': 'myusername',
...     'password': 'mypassword',
...     'database': 'mydatabase'}

Database connection configuration read from config file:

>>> connection = database_connect(
...     host=CONFIG['host'],
...     port=CONFIG['port'],
...     username=CONFIG['username'],
...     password=CONFIG['password'],
...     database=CONFIG['database'])

Or:

>>> connection = database_connect(**CONFIG)


Use Case - 0x04
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0
>>>
>>>
>>> MOVEMENT = [(0, 0),
...             (1, 0),
...             (2, 1, 1),
...             (3, 2),
...             (3, 3, -1),
...             (2, 3)]


>>> movement = [Point(x,y) for x,y in MOVEMENT]
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)


>>> movement = [Point(*coordinates) for coordinates in MOVEMENT]
>>>
>>> movement  # doctest: +NORMALIZE_WHITESPACE
[Point(x=0, y=0, z=0),
 Point(x=1, y=0, z=0),
 Point(x=2, y=1, z=1),
 Point(x=3, y=2, z=0),
 Point(x=3, y=3, z=-1),
 Point(x=2, y=3, z=0)]


Use Case - 0x04
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> result = [Iris(*row) for row in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]


Use Case - 0x05
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> DATA = [{"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_width":1.9,"species":"virginica"},
...         {"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2,"species":"setosa"},
...         {"sepal_length":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"species":"versicolor"},
...         {"sepal_length":6.3,"sepal_width":2.9,"petal_length":5.6,"petal_width":1.8,"species":"virginica"},
...         {"sepal_length":6.4,"sepal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versicolor"},
...         {"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"petal_width":0.2,"species":"setosa"}]
>>>
>>>
>>> result = [Iris(**row) for row in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]


Use Case - 0x06
---------------
Calling function with all variables from higher order function. ``locals()``
will return a ``dict`` with all the variables in local scope of the function:

>>> def template(template, **user_data):
...     print('Template:', template)
...     print('Data:', user_data)
>>>
>>>
>>> def controller(firstname, lastname, uid=0):
...     groups = ['admins', 'astronauts']
...     permission = ['all', 'everywhere']
...     return template('user_details.html', **locals())
>>>
>>>     # template('user_details.html',
>>>     #    firstname='Mark',
>>>     #    lastname='Watney',
>>>     #    uid=0,
>>>     #    groups=['admins', 'astronauts'],
>>>     #    permission=['all', 'everywhere'])
>>>
>>>
>>> controller('Mark', 'Watney')  # doctest: +NORMALIZE_WHITESPACE
Template: user_details.html
Data: {'firstname': 'Mark',
       'lastname': 'Watney',
       'uid': 0,
       'groups': ['admins', 'astronauts'],
       'permission': ['all', 'everywhere']}


Use Case - 0x07
---------------
* Definition of pandas.read_csv() function [#pandasreadcsv]_
* Proxy functions. One of the most common use of ``*args``, ``**kwargs``:

>>> def read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer',
...              names=None, index_col=None, usecols=None, squeeze=False,
...              prefix=None, mangle_dupe_cols=True, dtype=None, engine=None,
...              converters=None, true_values=None, false_values=None,
...              skipinitialspace=False, skiprows=None, nrows=None,
...              na_values=None, keep_default_na=True, na_filter=True,
...              verbose=False, skip_blank_lines=True, parse_dates=False,
...              infer_datetime_format=False, keep_date_col=False,
...              date_parser=None, dayfirst=False, iterator=False,
...              chunksize=None, compression='infer', thousands=None,
...              decimal=b'.', lineterminator=None, quotechar='"', quoting=0,
...              escapechar=None, comment=None, encoding=None, dialect=None,
...              tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True,
...              skipfooter=0, doublequote=True, delim_whitespace=False,
...              low_memory=True, memory_map=False, float_precision=None): ...

Proxy functions allows for changing defaults to the original function. One
simply define a function which has sensible defaults and call the original
function setting default values automatically. Thanks to using ``**kwargs``
there is no need to specify all the values from the original function. The
uncovered arguments will simply be put in ``kwargs`` dictionary and passed
to the original function:

>>> def mycsv(file, encoding='utf-8', delimiter=';', decimal=b',',
...           lineterminator='\n', **kwargs):
...     return read_csv(file, encoding=encoding, delimiter=delimiter,
...                     decimal=decimal, lineterminator=lineterminator,
...                     **kwargs)

This allows for cleaner code. Each parameter will be passed to ``mycsv``
function. Then it will be checked if there is a different default value
already defined. If not, then parameter will be stored in ``kwargs`` and
passed to the original function:

>>> mycsv('iris1.csv')
>>> mycsv('iris2.csv', encoding='iso-8859-2')
>>> mycsv('iris3.csv', encoding='cp1250', verbose=True)
>>> mycsv('iris4.csv', verbose=True, usecols=['Sepal Length', 'Species'])


Use Case - 0x08
---------------
Decorators are functions, which get reference to the decorated function as
it's argument, and has closure which gets original function arguments as
positional and keyword arguments:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper

Decorators could be used on any function, therefore we could not predict what
would be the name of the parameter passed to it:

>>> @mydecorator
... def add(a, b):
...     return a + b

>>> @mydecorator
... def echo(text):
...     return text

Moreover it depends on a user whether he/she chooses to run function
positionally, using keyword arguments or even both at the same time:

>>> add(1, 2)
3

>>> add(a=1, b=2)
3

>>> add(1, b=2)
3


References
----------
.. [#pandasreadcsv] The pandas development team. API Reference Pandas.read_csv(). Year: 2021. Retrieved: 2021-12-05. URL: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html


Assignments
-----------
.. literalinclude:: assignments/unpack_arguments_a.py
    :caption: :download:`Solution <assignments/unpack_arguments_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_arguments_b.py
    :caption: :download:`Solution <assignments/unpack_arguments_b.py>`
    :end-before: # Solution
