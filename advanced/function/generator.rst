.. _Generators:

**********
Generators
**********


Generator expressions vs. Comprehensions
========================================
.. code-block:: python

    list(x for x in range(0,5))        # [0, 1, 2, 3, 4]
    [x for x in range(0,5)]            # [0, 1, 2, 3, 4]

    set(x for x in range(0,5))         # {0, 1, 2, 3, 4}
    {x for x in range(0,5)}            # {0, 1, 2, 3, 4}

    dict((x,x) for x in range(0,5))    # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    {x: x for x in range(0,5)}         # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    tuple(x for x in range(0,5))       # (0, 1, 2, 3, 4)
    (x for x in range(0,5))            # <generator object <genexpr> at 0x118c1aed0>

    all(x for x in range(0,5))         # False
    any(x for x in range(0,5))         # True
    sum(x for x in range(0,5))         # 10

What is the difference?
-----------------------
.. highlights::
    * Comprehensions executes instantly
    * Generators are lazy evaluated
    * Create generator object and assign pointer (do not execute)
    * Comprehensions will be in the memory until end of a program
    * Generators are cleared once they are executed

    .. code-block:: python

        a = [x for x in range(0, 5)]

        print(a)
        # [0, 1, 2, 3, 4]

        print(a)
        # [0, 1, 2, 3, 4]

    .. code-block:: python

        a = (x for x in range(0, 5))

        print(a)
        # <generator object <genexpr> at 0x111e7acd0>

        print(list(a))
        # [0, 1, 2, 3, 4]

        print(list(a))
        # []


Lazy evaluation
===============
.. highlights::
    * Code do not execute instantly
    * Sometimes code is not executed at all!

Declaring generators
--------------------
.. code-block:: python
    :caption: This will not generate any numbers!

    a = (x for x in range(0,5))
    b = (x for x in range(0,5))
    c = (x for x in range(0,5))

.. code-block:: python
    :caption: This will only create generator expression, but not evaluate it!

    a = (x for x in range(0,5))

    print(a)
    # <generator object <genexpr> at 0x11cb45950>

Evaluating generator instantly
------------------------------
.. highlights::
    * Not very efficient
    * If you need values evaluated instantly, there is no point in using generators

.. code-block:: python

    a = (x for x in range(0,5))

    list(a)
    # [0, 1, 2, 3, 4]

Evaluate generator iteratively
------------------------------
.. highlights::
    * Generator will calculate next number for every loop iteration
    * Forgets previous number
    * Doesn't know the next number

.. code-block:: python

    a = (x for x in range(0,5))

    for i in a:
        print(i)
    # 0
    # 1
    # 2
    # 3
    # 4

Halting and resuming iteration
------------------------------
.. highlights::
    * Will generate only three numbers, then stop
    * Forget generator

.. code-block:: python
    :caption: Comprehension will generate a sequence instantly, and iterate over it. It will be in the memory until end of a program

    numbers = [x for x in range(0, 10)]

    for x in numbers:
       print(x)
       if x == 3:
           break
    # 0
    # 1
    # 2
    # 3

    for x in numbers:
       print(x)
       if x == 6:
           break
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

    list(numbers)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    list(numbers)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python
    :caption: Generator with generate numbers as it goes in the process

    numbers = (x for x in range(0, 10))

    for x in numbers:
       print(x)
       if x == 3:
           break
    # 0
    # 1
    # 2
    # 3

    for x in numbers:
       print(x)
       if x == 6:
           break
    # 4
    # 5
    # 6

    list(numbers)
    # [7, 8, 9]

    list(numbers)
    # []

Which one is better?
--------------------
.. highlights::
    * Comprehensions - Using values more than one
    * Generators - Using values once (for example in the loop iterator)


``yield`` Operator
==================
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

    def get_species(species):
        result = []
        for row in DATA:
            if row[4] == species:
                result.append(row)
        return result


    data = get_species('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
    #  (5.4, 3.9, 1.7, 0.4, 'setosa')]

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

    def get_species(species):
        for row in DATA:
            if row[4] == species:
                yield row

    data = get_species('setosa')

    print(data)
    # <generator object get_species at 0x11af257c8>

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')


Built-in generators
===================

``zip()``
---------
.. code-block:: python
    :caption: ``map()`` syntax

    zip(<sequence>, <sequence>, ...)

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]

    zip(header, data)
    # <zip object at 0x11cf54b90>

    list(zip(header, data))
    # [('a', 1), ('b', 2), ('c', 3)]

    tuple(zip(header, data))
    # (('a', 1), ('b', 2), ('c', 3))

    dict(zip(header, data))
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    row = [77,88,99]

    [(h,d,r) for h,d,r in zip(header, data, row)]
    # [('a', 1, 77), ('b', 2, 88), ('c', 3, 99)]

``map()``
---------
.. code-block:: python
    :caption: ``map()`` syntax

    map(<callable>, <sequence>)

.. code-block:: python

    data = [1, 2, 3]

    list(map(float, data))
    # [1.0, 2.0, 3.0]

.. code-block:: python

    map(float, [1, 2, 3])
    # <map object at 0x11d15a190>

    list(map(float, [1, 2, 3]))
    # [1.0, 2.0, 3.0]

    tuple(map(float, [1, 2, 3]))
    # (1.0, 2.0, 3.0)

``filter()``
------------
.. code-block:: python
    :caption: ``filter()`` syntax

    filter(<callable>, <sequence>)

.. code-block:: python
    :caption: Show only even numbers

    data = [1, 2, 3, 4, 5, 6]

    list(filter(lambda x: x % 2 == 0, data))
    # [2, 4, 6]

.. code-block:: python

    data = [1, 2, 3, 4, 5, 6]

    def is_even(x):
        return x % 2 == 0

    filter(is_even, data)
    # <filter object at 0x11d182990>

    list(filter(is_even, data))
    # [2, 4, 6]

.. code-block:: python

    data = [1, 2, 3, 4, 5, 6]

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    filter(is_even, data)
    # <filter object at 0x11d182990>

    list(filter(is_even, data))
    # [2, 4, 6]

.. code-block:: python
    :caption: ``filter()`` example

    DATA = [
        {'name': 'Jan Twardowski', 'age': 21},
        {'name': 'Mark Watney', 'age': 25},
        {'name': 'Melissa Lewis', 'age': 18},
    ]

    def is_adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    result = filter(is_adult, DATA)
    print(list(result))
    # [
    #   {'name': 'Jan Twardowski', 'age': 21},
    #   {'name': 'Mark Watney', 'age': 25},
    # ]

``enumerate()``
---------------
.. code-block:: python
    :caption: ``enumerate()`` syntax

    enumerate(<sequence>)

.. code-block:: python

    data = ['a', 'b', 'c']

    list(enumerate(data))
    # [(0, 'a'), (1, 'b'), (2, 'c')]

    dict(enumerate(data))
    # {0: 'a', 1: 'b', 2: 'c'}

    dict((v,k) for k,v in enumerate(data))
    # {'a': 0, 'b': 1, 'c': 2}

    {v:k for k,v in enumerate(data, start=5)}
    # {'a': 5, 'b': 6, 'c': 7}

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i, _ in enumerate(header):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i, header in enumerate(header):
        result[header] = data[i]

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}


Generator as Iterator
=====================
.. code-block:: python

    a = (x for x in range(0,3))

    next(a)
    # 0

    next(a)
    # 1

    next(a)
    # 2

    next(a)
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # StopIteration


.. code-block:: python

    data = (x for x in range(0,3))

    for a in data:
        print(a)

    # is analogous to:
    try:
        i = iter(data)

        a = next(i)
        print(a)

        a = next(i)
        print(a)

        a = next(i)
        print(a)

        a = next(i)
        print(a)

        a = next(i)
        print(a)
    except StopIteration:
        pass


Assignments
===========

Function Generator Iris
-----------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/function_generator_iris.py`

:English:
    #. Use code from "Input" section (see below)
    #. Download :download:`data/iris.csv` and save as `iris.csv`
    #. Read data skipping header
    #. Create function with returns all measurements for given species
    #. Species will be passed as an ``str`` argument to the function
    #. Implement solution using normal function
    #. Implement solution using generator and ``yield`` keyword
    #. Compare results of both using ``sys.getsizeof()``
    #. What will happen if input data will be bigger?

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Pobierz :download:`data/iris.csv` i zapisz jako `iris.csv`
    #. Zaczytaj dane pomijając nagłówek
    #. Napisz funkcję która zwraca wszystkie pomiary dla danego gatunku
    #. Gatunek będzie podawany jako argument typu ``str`` do funkcji
    #. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
    #. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
    #. Porównaj wyniki obu używając ``sys.getsizeof()``
    #. Co się stanie, gdy ilość danych będzie większa?

:The whys and wherefores:
    * Using generators
    * Unpacking lazy evaluated code
    * Comparing size of objects
    * Parsing CSV file
    * Filtering file content

:Input:
    .. code-block:: python

        with open(r'iris.csv') as file:
            data = file.read()

        fun = function_filter(data, 'setosa')
        gen = generator_filter(data, 'setosa')

        print('Function', sys.getsizeof(fun))
        print('Generator', sys.getsizeof(gen))

Function Generator Passwd
-------------------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/function_generator_passwd.py`

:English:
    #. Download :download:`data/hosts.txt` and save as `hosts.txt`
    #. Iterating over lines, filter out comments, empty lines, etc.
    #. Extract system accounts (users with UID [third field] is less than 1000)
    #. Return list of system account logins
    #. Implement solution using normal function
    #. Implement solution using generator and ``yield`` keyword
    #. Compare results of both using ``sys.getsizeof()``
    #. What will happen if input data will be bigger?

:Polish:
    #. Pobierz :download:`data/hosts.txt` i zapisz jako `hosts.txt`
    #. Iterując po liniaj, odfiltruj komentarze, puste linie itp.
    #. Wyciągnnij konta systemowe (użytkownicy z UID (trzecie pole) mniejszym niż 1000)
    #. Zwróć listę loginów użytkowników systemowych
    #. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
    #. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
    #. Porównaj wyniki obu używając ``sys.getsizeof()``
    #. Co się stanie, gdy ilość danych będzie większa?

:The whys and wherefores:
    * Using generators
    * Unpacking lazy evaluated code
    * Comparing size of objects
    * Parsing CSV file
    * Filtering file content
