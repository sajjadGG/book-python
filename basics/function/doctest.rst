.. _Function Doctest:

****************
Function Doctest
****************


.. highlights::
    * tests are always the most up-to-date code documentation
    * tests cannot get out of sync from code
    * checks if function output is exactly as expected
    * useful for regex modifications
    * can add text (i.e. explanations) between tests
    * Case Study: https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_base.py#L409
    * PyCharm doctest runner warns about ``DeprecationWarning``, fix in progress -  https://youtrack.jetbrains.com/issue/PY-31751

Syntax
======
.. highlights::
    * Docstring is a first multiline comment in:

        * File / Module
        * Class
        * Method / Function

    * It is accessible in ``__doc__`` property of an object
    * Used for generating ``help()`` documentation
    * Used for ``doctest``
    * :pep:`257` Docstring convention - For multiline always use three double quote (``"""``) characters

.. code-block:: python
    :caption: Docstring used for documentation

    def apollo_dsky(noun, verb):
        """
        This is the Apollo Display Keyboard
        It takes noun and verb
        """
        print(f'Program selected. Noun: {noun}, verb: {verb}')

.. code-block:: python
    :caption: Docstring used for doctest

    def add(a, b):
        """
        Sums two numbers.

        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
        """
        return a + b


Running tests
=============

Running tests with your IDE
---------------------------
.. highlights::
    * View menu -> Run... -> Doctest in ``my_function``

From code
---------
.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

From command line
-----------------
.. code-block:: console
    :caption: Display only errors. With ``-v`` display progress

    $ python -m doctest example.py
    $ python -m doctest -v example.py


Test Numeric Values
===================
.. code-block:: python
    :caption: ``int`` values

    def add_numbers(a, b):
        """
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(-1, 1)
        0
        >>> add_numbers(0, 0)
        0
        """
        return a + b

.. code-block:: python
    :caption: ``float`` values

    def add_numbers(a, b):
        """
        >>> add_numbers(2.5, 1.2)
        3.7

        >>> add_numbers(0.1, 0.2)
        0.30000000000000004

        >>> add_numbers(0.1, 0.2)  # doctest: +ELLIPSIS
        0.3000...
        """
        return a + b


Testing Logic Values
====================
.. code-block:: python

    AGE_ADULT = 18

    def is_adult(age):
        """
        Function checks if person is adult.
        Adult person is over 18 years old.

        >>> is_adult(18)
        True

        >>> is_adult(17.9)
        False
        """
        if age >= AGE_ADULT:
            return True
        else:
            return False

.. code-block:: python
    :caption: This test will fail. Expected exception, got 2.0

    def add_numbers(a, b):
        """
        >>> add_numbers(True, 1)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        """
        if not isinstance(a, (int, float)):
            raise ValueError('not a number')

        if not isinstance(b, (int, float)):
            raise ValueError('not a number')

        return a + b

    # Expected:
    #     Traceback (most recent call last):
    #         ...
    #     ValueError: not a number
    # Got:
    #     2.0

.. code-block:: python
    :caption: This test will pass.

    def add_numbers(a: float, b: float) -> float:
        """
        >>> add_numbers(True, 1)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        """
        if type(a) not in (int, float):
            raise ValueError('not a number')

        if type(b) not in (int, float):
            raise ValueError('not a number')

        return a + b


Testing String Values
=====================
.. highlights::
    * Python will change to single quotes in most cases
    * Python will change to double quotes to avoid escapes

.. code-block:: python
    :caption: Returning ``str``. Python will change to single quotes in most cases
    :emphasize-lines: 3-4,7-8,11-12,15-16

    def echo(text):
        """
        >>> echo('hello')
        'hello'

        # Python will change to single quotes in most cases
        >>> echo("hello")
        'hello'

        Following test will fail
        >>> echo('hello')
        "hello"

        Python will change to double quotes to avoid escapes
        >>> echo('It\\'s Twardowski\\'s Moon')
        "It's Twardowski's Moon"
        """
        return text

Testing ``print()``
-------------------
.. highlights::
    * ``print()`` function output, don't have quotes

.. code-block:: python
    :caption: There are no quotes in ``print()`` function output
    :emphasize-lines: 4

    def echo(text):
        """
        >>> echo('hello')
        hello
        """
        print(text)

.. code-block:: python
    :caption: Testing ``print(str)`` with newlines
    :emphasize-lines: 7

    def echo(text):
        """
        >>> echo('hello')
        hello
        hello
        hello
        <BLANKLINE>
        """
        print(f'{text}\n' * 3)


Testing for exceptions
======================
.. code-block:: python
    :caption: Testing for exceptions
    :emphasize-lines: 3-6

    def add_numbers(a, b):
        """
        >>> add_numbers('one', 'two')
        Traceback (most recent call last):
            ...
        TypeError: Argument must be int or float
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Argument must be int or float')

        if not isinstance(b, (int, float)):
            raise TypeError('Argument must be int or float')

        return a + b


Using python statements
=======================
.. code-block:: python
    :caption: Using python statements in ``doctest``
    :emphasize-lines: 3-5

    def when(date):
        """
        >>> from datetime import datetime, timezone
        >>> moon = datetime(1969, 7, 21, 17, 54, tzinfo=timezone.utc)
        >>> when(moon)
        1969-07-21 17:54 UTC
        """
        print(f'{date:%Y-%m-%d %H:%M %Z}')


Examples
========

Adding two numbers
------------------
.. code-block:: python
    :caption: Adding two numbers

    def add_numbers(a: float, b: float) -> float:
        """
        >>> add_numbers(1, 2)
        3.0
        >>> add_numbers(-1, 1)
        0.0
        >>> add_numbers(0.1, 0.2)  # doctest: +ELLIPSIS
        0.3000...
        >>> add_numbers(1.5, 2.5)
        4.0
        >>> add_numbers(1, 1.5)
        2.5
        >>> add_numbers([1, 2], 3)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        >>> add_numbers(0, [1, 2])
        Traceback (most recent call last):
            ...
        ValueError: not a number
        >>> add_numbers('one', 'two')
        Traceback (most recent call last):
            ...
        ValueError: not a number
        >>> add_numbers(True, 1)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        """
        if type(a) not in (int, float):
            raise ValueError('not a number')

        if type(b) not in (int, float):
            raise ValueError('not a number')

        return float(a + b)


Celsius to Kelvin temperature conversion
----------------------------------------
.. code-block:: python
    :caption: Celsius to Kelvin temperature conversion

    def celsius_to_kelvin(temperature_in_celsius):
        """
        >>> celsius_to_kelvin(0)
        273.15

        >>> celsius_to_kelvin(1)
        274.15

        >>> celsius_to_kelvin(-1)
        272.15

        >>> celsius_to_kelvin(-273.15)
        0.0

        >>> celsius_to_kelvin(-274.15)
        Traceback (most recent call last):
            ...
        ValueError: Argument must be greater than -273.15

        >>> celsius_to_kelvin([-1, 0, 1])
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float

        >>> celsius_to_kelvin('one')
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float
        """
        if not isinstance(temperature_in_celsius, (float, int)):
            raise ValueError('Argument must be int or float')

        if temperature_in_celsius < -273.15:
            raise ValueError('Argument must be greater than -273.15')

        return float(temperature_in_celsius + 273.15)


Assignments
===========

Refactoring
-----------
* Complexity level: easy
* Lines of code to write: 5 lines of code
* Estimated time of completion: 15 min
* Solution: :download:`solution/function_doctest_temp.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write implementation of a function ``celsius_to_kelvin``
    #. All tests must pass

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Napisz implementację funkcji ``celsius_to_kelvin``
    #. Wszystkie testy muszą przechodzić

:Input:
    .. code-block:: python

        def celsius_to_kelvin(degrees):
            """
            >>> celsius_to_kelvin(0)
            273.15
            >>> celsius_to_kelvin(1)
            274.15
            >>> celsius_to_kelvin(-1)
            272.15
            >>> celsius_to_kelvin('a')
            Traceback (most recent call last):
                ...
            TypeError: Invalid argument
            >>> celsius_to_kelvin([0, 1])
            [273.15, 274.15]
            >>> celsius_to_kelvin((0, 1))
            (273.15, 274.15)
            >>> celsius_to_kelvin({0, 1})
            {273.15, 274.15}
            """
            return ...

Distance conversion doctest
---------------------------
* Complexity level: easy
* Lines of code to write: 5 lines of code + 16 lines of tests
* Estimated time of completion: 10 min
* Solution: :download:`solution/function_doctest_distance.py`

:English:
    #. Write functions which convert distance given in kilometers to meters
    #. 1 km = 1000 m
    #. Distance cannot be negative
    #. Returned value must by float
    #. Write doctests
    #. Compare result with "Output" section (see below)

:Polish:
    #. Napisz funkcję, która przeliczy dystans podany w kilometrach na metry
    #. 1 km = 1000 m
    #. Dystans nie może być ujemny
    #. Zwracany dystans musi być float
    #. Napisz doctesty
    #. Compare result with "Output" section (see below)

:Output:
    * Test arguments:

        * -1
        * 0
        * 1
        * ``float``
        * ``int``
        * ``str`` -> expect ``TypeError``
        * any other type -> expect ``TypeError``
        * True

Fix URL Regex
-------------
* Complexity level: hard
* Lines of code to write: 0 lines (**discussion only**)
* Estimated time of completion: 5 min

:English:
    #. Use data from "Input" section (see below)
    #. Pattern incorrectly classifies ``https://foo_bar.example.com/`` as invalid
    #. Fix pattern without automated tests
    #. Don't break classification of the other cases

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wyrażenie niepoprawnie klasyfikuje ``https://foo_bar.example.com/`` jako nieprawidłowy
    #. Popraw wyrażenie bez testów automatycznych
    #. Nie zepsuj klasyfikacji pozostałych przypadków

:Input:
    .. code-block:: python
        :caption: @diegoperini --  https://mathiasbynens.be/demo/url-regex

        PATTERN = r'_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS'

        VALID = [
            'http://foo.com/blah_blah',
            'http://foo.com/blah_blah/',
            'http://foo.com/blah_blah_(wikipedia)',
            'http://foo.com/blah_blah_(wikipedia)_(again)',
            'http://www.example.com/wpstyle/?p=364',
            'https://www.example.com/foo/?bar=baz&inga=42&quux',
            'http://✪df.ws/123',
            'http://userid:password@example.com:8080',
            'http://userid:password@example.com:8080/',
            'http://userid@example.com',
            'http://userid@example.com/',
            'http://userid@example.com:8080',
            'http://userid@example.com:8080/',
            'http://userid:password@example.com',
            'http://userid:password@example.com/',
            'http://142.42.1.1/',
            'http://142.42.1.1:8080/',
            'http://➡.ws/䨹',
            'http://⌘.ws',
            'http://⌘.ws/',
            'http://foo.com/blah_(wikipedia)#cite-1',
            'http://foo.com/blah_(wikipedia)_blah#cite-1',
            'http://foo.com/unicode_(✪)_in_parens',
            'http://foo.com/(something)?after=parens',
            'http://☺.damowmow.com/',
            'http://code.google.com/events/#&product=browser',
            'http://j.mp',
            'ftp://foo.bar/baz',
            'http://foo.bar/?q=Test%20URL-encoded%20stuff',
            'http://مثال.إختبار',
            'http://例子.测试',
            'http://उदाहरण.परीक्षा',
            'http://-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com',
            'http://1337.net',
            'http://a.b-c.de',
            'http://223.255.255.254',
            'https://foo_bar.example.com/',
        ]

        INVALID = [
            'http://',
            'http://.',
            'http://..',
            'http://../',
            'http://?',
            'http://??',
            'http://??/',
            'http://#',
            'http://##',
            'http://##/',
            'http://foo.bar?q=Spaces',
            '//',
            '//a',
            '///a',
            '///',
            'http:///a',
            'foo.com',
            'rdar://1234',
            'h://test',
            'http:// shouldfail.com',
            ':// should fail',
            'http://foo.bar/foo(bar)baz quux',
            'ftps://foo.bar/',
            'http://-error-.invalid/',
            'http://a.b--c.de/',
            'http://-a.b.co',
            'http://a.b-.co',
            'http://0.0.0.0',
            'http://10.1.1.0',
            'http://10.1.1.255',
            'http://224.1.1.1',
            'http://1.1.1.1.1',
            'http://123.123.123',
            'http://3628126748',
            'http://.www.foo.bar/',
            'http://www.foo.bar./',
            'http://.www.foo.bar./',
            'http://10.1.1.1',
            'http://10.1.1.254',
        ]
