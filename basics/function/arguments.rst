******************
Function Arguments
******************


Simple Usage
============
.. code-block:: python

    def add(a, b):
        print(a + b)

    add(1, 2)
    # 3

    add(1.5, 2.5)
    # 4.0

.. code-block:: python

    def echo(text):
        print(text)

    echo('hello')
    # hello


Required arguments
==================
.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract()
    # TypeError: subtract() missing 2 required positional arguments: 'a' and 'b'

    subtract(10)
    # TypeError: subtract() missing 1 required positional argument: 'b'

    subtract(10, 20)
    # -10

Arguments with default value
============================
.. highlights::
    * Arguments without default values are required
    * Function will take default value if not overwritten by user
    * Arguments with default values must be at the right side
    * Arguments with default values can be omitted while executing

.. code-block:: python

    def subtract(a=1, b=2):
        return a - b


    subtract()
    # -1

    subtract(10)
    # 8

    subtract(10, 20)
    # -10

.. code-block:: python

    def subtract(a, b=2):
        return a - b

.. code-block:: python

    def subtract(a=1, b):
        return a - b

    # SyntaxError: non-default argument follows default argument


Positional arguments
====================
.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(2, 1)      # 1
    subtract(1, 2)      # -1


Keyword arguments
=================
.. highlights::
    * Arguments without default values are required
    * Order of keyword arguments has no significance

.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(a=2, b=1)  # 1
    subtract(b=1, a=2)  # 1
    subtract(2, b=1)    # 1
    subtract(2, a=1)    # TypeError: subtract() got multiple values for argument 'a'
    subtract(a=2, 1)    # SyntaxError: positional argument follows keyword argument

.. code-block:: python

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Mark Watney')          # My name... Mark Watney
    hello(name='Mark Watney')     # My name... Mark Watney
    hello()                       # My name... José Jiménez


Example
=======
.. code-block:: python

    def connect(username, password, host='127.0.0.1',
                port=80, ssl=True, keep_alive=1, persistent=False):
        print('Connecting...')


    connect('admin', 'admin', 'localhost', 80, False, 1, True)

    connect(host='localhost', username='admin', password='admin', ssl=True, persistent=True, keep_alive=1)

    connect(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )

.. code-block:: python

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

    my_file1 = read_csv('iris.csv')
    my_file2 = read_csv('iris.csv', encoding='utf-8')
    my_file3 = read_csv('iris.csv', encoding='utf-8', parse_dates=['date_of_birth'])
    my_file4 = read_csv('iris.csv', skiprows=3, delimiter=';')
    my_file5 = read_csv('iris.csv',
        encoding='utf-8',
        skiprows=3,
        delimiter=';',
        usecols=['Sepal Length', 'Species'],
        parse_dates=['date_of_birth']
    )
