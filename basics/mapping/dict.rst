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

    data = {}
    data = dict()

    data = {'a': 1, 'b': 2}

    data = {
        1: 'Mark Watney',
        2: 'Jan Twardowski'}

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski'}

    data = dict(
        first_name='Jan',
        last_name='Twardowski')

.. code-block:: python
    :caption: Duplicating items are overridden by latter

    data = {
        'species': 'setosa',
        'species': 'virginica',
    }
    # {'species': 'virginica'}


Getting Items
=============
.. highlights::
    * ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
    * ``.get()`` returns ``None`` if key not found
    * ``.get()`` can have default value, if key not found

.. code-block:: python
    :caption: Getitem Method

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    data['last_name']
    # Twardowski

    data['agency']
    # KeyError: 'agency'

.. code-block:: python
    :caption: Get Method

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    data.get('last_name')
    # Twardowski

    data.get('agency')
    # None

    data.get('agency', 'unknown')
    # 'unknown'

.. code-block:: python
    :caption: Getting keys other than ``str``

    data = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    data[1961]
    # 'First Human Space Flight'

    data.get(1961)
    # 'First Human Space Flight'

    data['1961']
    # KeyError: '1961'

    data.get('1961')
    # None

    data.get('1961', 'unknown')
    # 'unknown'

Get Keys, Values and Key-Value Pairs
------------------------------------
* Key can be any hashable object

.. code-block:: python

    data = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9,
    }

    list(data.keys())
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']

    list(data.values())
    # [5.8, 2.7, 5.1, 1.9]

    list(data.items())
    # [
    #     ('Sepal length', 5.8),
    #     ('Sepal width', 2.7),
    #     ('Petal length', 5.1),
    #     ('Petal width', 1.9),
    # ]


Setting Items
=============
.. highlights::
    * Adds if value not exist
    * Updates if value exist

.. code-block:: python
    :caption: Setitem Method

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    data['agency'] = 'POLSA'

    print(data)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA'
    # }

.. code-block:: python
    :caption: Update Method

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    data.update(agency='POLSA')
    print(data)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA'
    # }

    data.update(mission=['Apollo', 'Artemis', 'Ares'])
    print(data)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski',
    #   'agency': 'POLSA',
    #   'mission': ['Apollo', 'Artemis', 'Ares']
    # }

.. code-block:: python
    :caption: Update Method

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
    }

    more = {
        'agency': 'POLSA',
        'mission': ['Apollo', 'Artemis', 'Ares'],
    }

    data.update(more)
    print(data)
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

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    value = data.pop('agency')

    print(data)
    # {'first_name', 'Jan',
    #  'last_name': 'Twardowski'}

    print(value)
    # 'POLSA'

.. code-block:: python
    :caption: Popiitem Method

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    value = data.popitem()

    print(data)
    # {'first_name', 'Jan',
    #  'last_name': 'Twardowski'}

    print(value)
    # ('agency', 'POLSA')

.. code-block:: python
    :caption: Del Keyword

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    del data['agency']

    print(data)
    # {'first_name': 'Jan',
    #  'last_name': 'Twardowski'}


Indexing and Slicing
====================
.. highlights::
    * Indexing on ``dict`` is not possible
    * Slicing on ``dict`` is not possible

.. code-block:: python

    data = {
        'a': 0,
        'b': 1,
        'c': 2,
    }

    data[0]             # KeyError: 0
    data[1]             # KeyError: 1
    data[2]             # KeyError: 2

    data[-0]            # KeyError: 0
    data[-1]            # KeyError: -1
    data[-2]            # KeyError: -2

    data[1:2]           # TypeError: unhashable type: 'slice'
    data[:2]            # TypeError: unhashable type: 'slice'
    data[::2]           # TypeError: unhashable type: 'slice'

.. code-block:: python

    data = {
        0: 'a',
        1: 'b',
        2: 'c',
    }

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'

    data[-0]            # 'a'
    data[-1]            # KeyError: -1
    data[-2]            # KeyError: -2

    data[1:2]           # TypeError: unhashable type: 'slice'
    data[:2]            # TypeError: unhashable type: 'slice'
    data[::2]           # TypeError: unhashable type: 'slice'


``dict`` vs. ``set``
====================
.. highlights::
    * Both ``set`` and ``dict`` keys must be hashable
    * Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
    * Despite similar syntax, they are different types

.. code-block:: python

    {1, 2}            # set
    {1: 2}            # dict

    {1, 2, 3, 4}      # set
    {1: 2, 3: 4}      # dict

.. code-block:: python
    :caption: Empty ``dict`` and empty ``set``

    data = {1: 1}       # {1:1}
    data.pop(1)         # {}

    data = {1}          # {1}
    data.pop()          # set()

.. code-block:: python
    :caption: Differences

    data = {1: 1}
    isinstance(data, set)          # False
    isinstance(data, dict)         # True

    data = {1}
    isinstance(data, set)          # True
    isinstance(data, dict)         # False

    data = {}
    isinstance(data, (set, dict))  # True
    isinstance(data, set)          # False
    isinstance(data, dict)         # True


Length
======
.. code-block:: python

    data = {
        'first_name': 'Jan',
        'last_name': 'Twardowski',
        'agency': 'POLSA',
    }

    len(data)
    # 3

    len(data.keys())
    # 3

    len(data.values())
    # 3

    len(data.items())
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
* Solution: :download:`solution/mapping_dict_get.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create translator of pilot's alphabet
    #. Each letter has it's phonetic counterpart
    #. To convert table use multiline select with ``alt`` key in your IDE (if shortcut key is not working in your IDE, use only first four letters)
    #. Ask user to input letter
    #. User will always put only one capitalized letter or number
    #. Print phonetic letter pronunciation
    #. If user type character not existing in alphabet, print: "Pilots don't say that"
    #. Do not use ``if``, ``try``, and ``except``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
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
