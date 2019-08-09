********
``dict``
********


* ``dict`` are key-value storage
* Mutable - can add, remove, and modify items


Initializing
============

Initialize empty
----------------
.. code-block:: python

    my_dict = {}
    my_dict = dict()

Initialize with many elements
-----------------------------
* Comma after last element is optional

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski'
    }

.. code-block:: python

    my_dict = dict(
        first_name='Jan',
        last_name='Twardowski'
    )

Duplicating items are overridden by latter
------------------------------------------
.. code-block:: python

    my_dict = {
        'name': 'Twardowski',
        'name': 'Иванович',
    }
    # {'name': 'Иванович'}

Key can be any hashable object
------------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

.. code-block:: python

    my_dict = {
        (1,): 'tuple with one element',
        (2, 3, 4): 'tuple with many elements',
    }

.. code-block:: python

    key = 'last_name'

    my_dict = {
        'fist_name': 'key can be str',
        1: 'key can be int',
        1.5: 'key can be float',
        (1,): 'key can be tuple',
        (2, 3, 4): 'key can be tuple',
        key: 'key can be str',
    }

Value can be any object
-----------------------
.. code-block:: python

    my_dict = {
        'date': '1969-07-21',
        'age': 42,
        'astronaut': {'name': 'Jan Twardowski', 'medals': {'Medal of Honor', 'Purple Heart'}},
        'agency': ['POLSA', 'Roscosmos', 'ESA'],
        'location': ('Baikonur', 'Johnson Space Center'),
    }

Order of ``dict`` elements
--------------------------
* Since Python 3.7 ``dict`` keeps order of elements
* Before Python 3.7 ``dict`` order is not ensured!!

.. note:: Since Python 3.7: The insertion-order preservation nature of dict objects is now an official part of the Python language spec.


Adding elements
===============
* Adds if value not exist
* Updates if value exist

Adding using ``[...]`` syntax
-----------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict['agency'] = 'POLSA'

    print(my_dict)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA'
    # }

Adding using ``.update()`` method
---------------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.update(agency='POLSA')
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA'
    # }

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.update(agency=['POLSA', 'ESA', 'Roscosmos'])
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': ['POLSA', 'ESA', 'Roscosmos']
    # }

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.update({'agency': 'POLSA'})
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA'
    # }


Removing items
==============

``.pop()``
----------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    value = my_dict.pop('agency')

    my_dict  # {'first_name', 'Jan', 'last_name': 'Twardowski'}
    value    # 'POLSA'

``del`` keyword
---------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    del my_dict['agency']

    my_dict
    # {'first_name': 'Jan', 'last_name': 'Twardowski'}

Accessing elements
==================

Check if value in ``dict``
--------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    'first_name' in my_dict
    # True

    'agency' in my_dict
    # False

Accessing values with ``[...]``
-------------------------------
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict['last_name']
    # Twardowski

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    my_dict[1961]
    # 'First Human Space Flight'

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict['agency']
    # KeyError: 'agency'

Accessing values with ``.get(...)``
-----------------------------------
* ``.get(...)`` returns ``None`` if key not found
* ``.get(...)`` can have default value, if key not found

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.get('last_name')
    # Twardowski

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    my_dict.get(1961)
    # 'First Human Space Flight'

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.get('agency')
    # None

    my_dict.get('agency', 'n/a')
    # 'n/a'

Accessing ``dict`` keys, values and key-value pairs
---------------------------------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'age': 42,
    }

    my_dict.keys()
    # ['first_name', 'last_name', 'age']

    my_dict.values()
    # ['Jan', 'Twardowski', 42]

    my_dict.items()
    # [
    #   ('first_name', 'Jan'),
    #   ('last_name', 'Twardowski'),
    #   ('age', 42)
    # ]


Create ``dict`` from two sequences
==================================
* ``zip`` is a generator
* ``zip`` will create a list of pairs (like ``dict.items()``)

.. code-block:: python

    keys =  ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    values = [5.8, 2.7, 5.1, 1.9, 'virginica']

    my_dict = dict(zip(keys, values))

    print(my_dict)
    # {
    #   'Sepal length': 5.8,
    #   'Sepal width': 2.7,
    #   'Petal length': 5.1,
    #   'Petal width': 1.9,
    #   'Species': 'virginica'
    # }


Length of a ``dict``
====================
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'age': 42,
    }

    len(my_dict)
    # 3

    len(my_dict.keys())
    # 3

    len(my_dict.values())
    # 3

    len(my_dict.items())
    # 3


Assignments
===========

Aviation Language
-----------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/dict_alphabet.py`

#. Stwórz słownik języka pilotów
#. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
#. Do przekonwertowania tabelki poniżej, wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE
#. Wczytaj od użytkownika literę
#. Użytkownik zawsze poda przynajmniej jedną literę, cyfrę lub znak specjalny, zawsze będzie to duża litera
#. Wypisz na ekranie nazwę fonetyczną litery
#. Jeżeli wpisał znak, który nie jest w alfabecie, to wypisz "Pilots don't say that"
#. Nie używaj konstrukcji ``if``, ani ``try`` i ``except``

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Rzutowanie i konwersja typów

.. code-block:: text
    :caption: Aviation language

    Letter, Pronounce
    A, Alfa
    B, Bravo
    C, Charlie
    D, Delta
    E, Echo
    F, Foxtrot
    G, Golf
    H, Hotel
    I, India
    J, Juliet
    K, Kilo
    L, Lima
    M, Mike
    N, November
    O, Oscar
    P, Papa
    Q, Quebec
    R, Romeo
    S, Sierra
    T, Tango
    U, Uniform
    V, Victor
    W, Whisky
    X, X-Ray
    Y, Yankee
    Z, Zulu
