.. _Mapping Dict:

****************
Mapping ``dict``
****************


.. highlights::
    * ``dict`` are key-value storage
    * Mutable - can add, remove, and modify items


Type Definition
===============
.. highlights::
    * ``{}`` is used more often
    * ``dict()`` is more readable
    * Comma after last element is optional
    * Since Python 3.7 ``dict`` keeps order of elements
    * Before Python 3.7 ``dict`` order is not ensured!!

.. code-block:: python

    my_dict = {}
    my_dict = dict()

.. code-block:: python
    :caption: Initialize with many elements

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski'
    }

    my_dict = dict(
        first_name='Jan',
        last_name='Twardowski'
    )

.. code-block:: python
    :caption: Duplicating items are overridden by latter

    my_dict = {
        'species': 'setosa',
        'species': 'virginica',
    }
    # {'species': 'virginica'}


Type Annotation
===============
.. code-block:: python

    my_dict: dict = {}
    my_dict: dict = dict()

.. code-block:: python

    from typing import Dict

    my_dict: Dict[int, str] = {
        0: 'setosa',
        1: 'virginica',
        2: 'versicolor',
    }

.. code-block:: python

    from typing import Dict

    my_dict: Dict[float, str] = {
        5.8: 'Sepal length',
        2.7: 'Sepal width',
        5.1: 'Petal length',
        1.9: 'Petal width',
    }

.. code-block:: python

    from typing import Dict

    my_dict: Dict[str, float] = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9,
    }


Contains
========
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    'first_name' in my_dict
    # True

    'agency' in my_dict
    # False


Getting Items
=============
.. highlights::
    * ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
    * ``.get()`` returns None if not found, but also allows to set default value

Getitem Method
--------------
.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict['last_name']
    # Twardowski

    my_dict['agency']
    # KeyError: 'agency'

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    my_dict[1961]
    # 'First Human Space Flight'

    my_dict['1961']
    # KeyError: '1961'

Get Method
----------
.. highlights::
    * ``.get()`` returns ``None`` if key not found
    * ``.get()`` can have default value, if key not found

.. code-block:: python

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.get('last_name')
    # Twardowski

    my_dict.get('agency')
    # None

    my_dict.get('agency', 'n/a')
    # 'n/a'

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    my_dict.get(1961)
    # 'First Human Space Flight'

    my_dict.get('1961')
    # None

    my_dict.get('1961', 'unknown')
    # 'unknown'

Get Keys, Values and Key-Value Pairs
------------------------------------
* Key can be any hashable object

.. code-block:: python

    my_dict = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9,
    }

    my_dict.keys()
    # dict_keys(['Sepal length', 'Sepal width', 'Petal length', 'Petal width'])

    list(my_dict.keys())
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

    my_dict.values()
    # dict_values([5.8, 2.7, 5.1, 1.9])

    list(my_dict.values())
    # [5.8, 2.7, 5.1, 1.9]

    my_dict.items()
    # dict_items([
    #     ('Sepal length', 5.8),
    #     ('Sepal width', 2.7),
    #     ('Petal length', 5.1),
    #     ('Petal width', 1.9),
    # ])

    list(my_dict.items())
    # [
    #     ('Sepal length', 5.8),
    #     ('Sepal width', 2.7),
    #     ('Petal length', 5.1),
    #     ('Petal width', 1.9),
    #     ('Species', 'virginica'),
    # ]


Setting Items
=============
.. highlights::
    * Adds if value not exist
    * Updates if value exist

.. code-block:: python
    :caption: Setitem Method

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

.. code-block:: python
    :caption: Update Method

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    my_dict.update(agency='POLSA')
    print(my_dict)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA'
    # }

    my_dict.update(mission=['Apollo', 'Artemis', 'Ares'])
    print(my_dict)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA',
    #   'mission': ['Apollo', 'Artemis', 'Ares']
    # }

.. code-block:: python
    :caption: Update Method

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    data = {
        'agency': 'POLSA',
        'mission': ['Apollo', 'Artemis', 'Ares'],
    }

    my_dict.update(data)
    print(my_dict)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA',
    #   'mission': ['Apollo', 'Artemis', 'Ares']
    # }


Deleting Items
==============
.. code-block:: python
    :caption: Pop Method

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    value = my_dict.pop('agency')

    print(my_dict)
    # {'first_name', 'Jan',
    #  'last_name': 'Twardowski'}

    print(value)
    # 'POLSA'

.. code-block:: python
    :caption: Del Keyword

    my_dict = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    del my_dict['agency']

    print(my_dict)
    # {'first_name': 'Jan',
    #  'last_name': 'Twardowski'}


Indexing and Slicing
====================
.. highlights::
    * Indexing on ``dict`` is not possible
    * Slicing on ``dict`` is not possible

.. code-block:: python

    DATA = {
        'a': 0,
        'b': 1,
        'c': 2,
    }

    DATA[0]             # KeyError: 0
    DATA[1]             # KeyError: 1
    DATA[2]             # KeyError: 2

    DATA[-0]            # KeyError: 0
    DATA[-1]            # KeyError: -1
    DATA[-2]            # KeyError: -2

    DATA[1:2]           # TypeError: unhashable type: 'slice'
    DATA[:2]            # TypeError: unhashable type: 'slice'
    DATA[::2]           # TypeError: unhashable type: 'slice'

.. code-block:: python

    DATA = {
        0: 'a',
        1: 'b',
        2: 'c',
    }

    DATA[0]             # 'a'
    DATA[1]             # 'b'
    DATA[2]             # 'c'

    DATA[-0]            # 'a'
    DATA[-1]            # KeyError: -1
    DATA[-2]            # KeyError: -2

    DATA[1:2]           # TypeError: unhashable type: 'slice'
    DATA[:2]            # TypeError: unhashable type: 'slice'
    DATA[::2]           # TypeError: unhashable type: 'slice'


``dict`` vs. ``set``
====================
.. highlights::
    * Both ``set`` and ``dict`` keys must be hashable
    * Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
    * Despite similar syntax, they are different types

.. code-block:: python

    {1, 2}            # set
    {1: 2}            # dict

.. code-block:: python

    {1, 2, 3, 4}      # set
    {1: 2, 3: 4}      # dict

    {1, 2,}           # set
    {1: 2,}           # dict

.. code-block:: python
    :caption: Empty ``dict``

    my_data = {1: 1}
    # {1:1}

    my_data.pop(1)
    # {}

.. code-block:: python
    :caption: Empty ``set``

    my_data = {1}
    # {1}

    my_data.pop()
    # set()

.. code-block:: python
    :caption: Differences

    my_data = {1: 1}
    isinstance(my_data, dict)         # True
    isinstance(my_data, set)          # False

    my_data = {1}
    isinstance(my_data, dict)         # False
    isinstance(my_data, set)          # True

    my_data = {}
    isinstance(my_data, (set, dict))  # True
    isinstance(my_data, dict)         # True
    isinstance(my_data, set)          # False


Length
======
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


Examples
========
.. code-block:: python

    git = {
        'ce16a8ce': 'commit/1',
        'cae6b510': 'commit/2',
        '895444a6': 'commit/3',
        'aef731b5': 'commit/4',
        '4a92bc79': 'branch/master',
        'b3bbd85a': 'tag/v1.0',
    }

New features
============
.. versionadded:: Python 3.9
    :pep:`584` merge (``|``) and update (``|=``) operators have been added to the built-in dict class.


Assignments
===========

Aviation Language
-----------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/dict_alphabet.py`

:English:
    #. Create translator of pilot's alphabet
    #. Each letter has it's phonetic counterpart
    #. To convert table use multiline select with ``alt`` key in your IDE (if shortcut key is not working in your IDE, use only first four letters)
    #. Ask user to input letter
    #. User will always put only one capitalized letter or number
    #. Print phonetic letter pronunciation
    #. If user type character not existing in alphabet, print: "Pilots don't say that"
    #. Do not use ``if``, ``try``, and ``except``

:Polish:
    #. Stwórz tłumacza alfabetu pilotów
    #. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
    #. Do przekonwertowania tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE (jeżeli skrót klawiszowy nie działa w Twoim IDE, użyj tylko cztery pierwsze litery)
    #. Poproś użytkownika o wprowadzenie litery
    #. Użytkownik zawsze poda tylko jedną dużą literę lub cyfrę
    #. Wypisz fonetyczną wymowę litery
    #. Jeżeli wpisał znak, który nie występuje w alfabecie, wypisz: "Pilots don't say that"
    #. Nie używaj ``if``, ``try`` ani ``except``

:Input:
    .. code-block:: text

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

:The whys and wherefores:
    * Defining ``dict`` with values
    * Type casting
