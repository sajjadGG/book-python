*****************************
Arbitrary Number of Arguments
*****************************


Positional arguments
====================
- ``*`` in this context, is not multiplication in mathematical sense
- ``*`` is used for positional arguments
- ``args`` is a convention, but you can use any name
- ``*args`` unpacks from ``tuple``, ``list`` or ``set``

.. code-block:: python
    :caption: Positional arguments passed directly

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(1, 2)

.. code-block:: python
    :caption: Positional arguments passed from sequence

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1, 2)
    echo(*args)


Keyword Arguments
=================
- ``**`` in this context, is not power in mathematical sense
- ``**`` is used for keyword arguments
- ``kwargs`` is a convention, but you can use any name
- ``**kwargs`` unpacks from ``dict``

.. code-block:: python
    :caption: Keyword arguments passed directly

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(a=1, b=2)

.. code-block:: python
    :caption: Keyword arguments passed from ``dict``

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    kwargs = {'a': 1, 'b': 2}
    echo(**kwargs)


Positional and Keyword Arguments
================================
.. code-block:: python
    :caption: Positional and keyword arguments passed directly

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(1, b=2)

.. code-block:: python
    :caption: Positional and keyword arguments passed from sequence and ``dict``

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1,)
    kwargs = {'b': 2}

    echo(*args, **kwargs)


Dynamically create objects
==========================

From sequence
-------------
.. code-block:: python

    DATA = (6.0, 3.4, 4.5, 1.6, 'versicolor')

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    iris = Iris(*DATA)
    iris.species
    # 'versicolor'

.. code-block:: python

    DATA = [
        (6.0, 3.4, 4.5, 1.6, 'versicolor'),
        (4.9, 3.1, 1.5, 0.1, "setosa"),
    ]

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'{self.species}'

    output = [Iris(*row) for row in DATA]
    print(output)
    # [versicolor, setosa]

From mapping
------------
.. code-block:: python

    DATA = {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"}

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    iris = Iris(**DATA)
    iris.species
    # 'versicolor'

.. code-block:: python

    DATA = [
        {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},
        {"sepal_length": 4.9, "sepal_width": 3.1, "petal_length": 1.5, "petal_width": 0.1, "species": "setosa"},
    ]

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'{self.species}'


    output = [Iris(**row) for row in DATA]
    print(output)
    # ['versicolor', 'setosa']


Examples
========

Creating complex numbers
------------------------
.. code-block:: python
    :caption: Defining complex number by passing keyword arguments directly

    complex(real=3, imag=5)
    # (3+5j)

.. code-block:: python
    :caption: Defining complex number by passing keyword arguments in ``dict``

    kwargs = {'real': 3, 'imag': 5}

    complex(**kwargs)
    # (3+5j)

Vectors
-------
.. code-block:: python
    :caption: Passing vector to the function

    def cartesian_coordinates(x, y, z):
        print(x)    # 1
        print(y)    # 0
        print(z)    # 1


    vector = (1, 0, 1)

    cartesian_coordinates(*vector)

Print formatting
----------------
* Now f-string formatting is preferred

.. code-block:: python
    :caption: ``str.format()`` expects keyword arguments, which keys are used in string. It is cumbersome to pass ``format(name=name, agency=agency)`` for every variable in the code.

    name = 'Jan Twardowski'
    agency = 'POLSA'

    output = "{agency} astronaut {name} first on the Moon".format(**locals())
    print(output)
    # POLSA astronaut Jan Twardowski first on the Moon

Common configuration
--------------------
.. code-block:: python
    :caption: Calling a function which has similar parameters

    def draw_line(x, y, color, type, width, markers):
        ...


    draw_line(x=1, y=2, color='red', type='dashed', width='2px', markers='disc')
    draw_line(x=3, y=4, color='red', type='dashed', width='2px', markers='disc')
    draw_line(x=5, y=6, color='red', type='dashed', width='2px', markers='disc')

.. code-block:: python
    :caption: Passing configuration to the function, which sets parameters from the config

    def draw_line(x, y, color, type, width, markers):
        ...


    style = {
        'color': 'red',
        'type': 'dashed',
        'width': '2px',
        'markers': 'disc',
    }

    draw_line(x=1, y=2, **style)
    draw_line(x=3, y=4, **style)
    draw_line(x=5, y=6, **style)

.. code-block:: python
    :caption: Database connection configuration read from config file

    config = {
        'host': 'localhost',
        'port': 5432,
        'username': 'my_username',
        'password': 'my_password',
        'database': 'my_database',
    }


    def database_connect(host, port, username, password, database):
        return ...


    connection = database_connect(**config)

Calling function with all variables from higher order function
--------------------------------------------------------------
.. code-block:: python
    :caption: Passing arguments to lower order function. ``locals()`` will return a ``dict`` with all the variables in local scope of the function.

    def lower(a, b, c, d, e):
        print(a, b, c, d, e)

    def higher(a, b, c=0):
        d = 4
        e = 5
        lower(**locals())
        # lower(a=1, b=2, c=0, d=4, e=5)


    higher(1, 2)
    # 1 2 0 4 5

Proxy functions
---------------
.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.
    :emphasize-lines: 2,6,10

    def read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer',
                 names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
                 mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
                 true_values=None, false_values=None, skipinitialspace=False,
                 skiprows=None, nrows=None, na_values=None, keep_default_na=True,
                 na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
                 infer_datetime_format=False, keep_date_col=False, date_parser=None,
                 dayfirst=False, iterator=False, chunksize=None, compression='infer',
                 thousands=None, decimal=b'.', lineterminator=None, quotechar='"',
                 quoting=0, escapechar=None, comment=None, encoding=None, dialect=None,
                 tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True,
                 skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True,
                 memory_map=False, float_precision=None):
        """
        Definition of pandas.read_csv() function
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        """


    def my_csv(file, encoding='utf-8', *args, **kwargs):
        return read_csv(file, encoding=encoding, *args, **kwargs)


    my_csv('iris1.csv')
    my_csv('iris2.csv', encoding='iso-8859-2')
    my_csv('iris3.csv', encoding='cp1250', verbose=True)
    my_csv('iris4.csv', verbose=True, usecols=['Sepal Length', 'Species'])

Decorators
----------
.. code-block:: python
    :caption: Decorators are functions, which get pointer to the decorated function as it's argument, and has closure which gets original function arguments as positional and keyword arguments.

    def login_required(original_function):

        def wrapper(*args, **kwargs):
            user = kwargs['request'].user

            if user.is_authenticated():
                return original_function(*args, **kwargs)
            else:
                print('Permission denied')

        return wrapper


    @login_required
    def edit_profile(request):
        ...


Assignments
===========

Iris
----
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/calling_kwargs.py`

:English:
    #. Download :download:`data/iris.csv` and save as ``iris.csv``
    #. Remove ``species`` column
    #. Separate header from measurements
    #. For each line extract values by splitting lines by coma ``,``
    #. Create ``output: List[dict]`` by zipping header and measurements:

        - key: column name from the header
        - value: measurement at the position

    #. Create function ``mean(**kwargs)``, function
    #. Iterate over ``output`` and call ``mean()`` by passing arguments as keywords
    #. Print mean for each row

:Polish:
    #. Pobierz plik :download:`data/iris.csv` i zapisz jako ``iris.csv``
    #. Usuń kolumnę ``species``
    #. Odseparuj nagłówek od pomiarów
    #. Wyciągnij wartości z każdej linii przez podział jej po przecinku ``,``
    #. Stwórz ``output: List[dict]`` poprzez scalenie nagłówka i pomiarów z każdego wiersza

        - klucz: nazwa kolumny z nagłówka
        - wartość: pomiar z odpowiedniej kolumny

    #. Stwórz funkcję ``mean(**kwargs)``
    #. Iterując po ``output`` wywołuj ``mean()`` podając argumenty nazwanie
    #. Wypisz średnią dla każdego wiersza

:Non-functional requirements:
    * Use only ``str.split()`` method
    * Don't use ``pandas``, ``numpy`` or ``csv`` etc.

:Output:
    .. code-block:: python

        header: list
        # ['sepal_length', 'sepal_width' ,'petal_length', 'petal_width']

        output: List[Dict[str, float]] = [
            {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4},
            {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8},
            {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6},
            ...
        ]

:Hint:
    * ``map(float, measurements)``
