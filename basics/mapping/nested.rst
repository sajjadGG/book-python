**************
Mapping Nested
**************

Dict keys
=========
.. code-block:: python

    my_dict = {
        (1,): 'setosa',
        (2,): 'virginica',
        (3,): 'versicolor',
    }

.. code-block:: python

    my_dict = {
        (5.8, 2.7, 5.1, 1.9): 'virginica',
        (5.1, 3.5, 1.4, 0.2): 'setosa',
        (5.7, 2.8, 4.1, 1.3): 'versicolor',
    }

.. code-block:: python

    my_dict = {
        {1}: 'setosa',
    }
    # TypeError: unhashable type: 'set'

    my_dict = {
        [1]: 'setosa',
    }
    # TypeError: unhashable type: 'list'


Dict values
===========
* Value can be any object

.. code-block:: python

    my_dict = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9,
    }

.. code-block:: python

    my_dict = {
        'virginica': (5.8, 2.7, 5.1, 1.9),
        'setosa': (5.1, 3.5, 1.4, 0.2),
        'versicolor': (5.7, 2.8, 4.1, 1.3),
    }

.. code-block:: python

    my_dict = {
        'virginica': [5.8, 2.7, 5.1, 1.9],
        'setosa': (5.1, 3.5, 1.4, 0.2),
        'versicolor': {5.7, 2.8, 4.1, 1.3},
    }

.. code-block:: python

    my_dict = {
        'commander': {'first_name': 'Jan', 'last_name': 'Twardowski'},
        'medical_officer': {'first_name': 'José', 'last_name': 'Jiménez'},
        'flight_engineer': {'first_name': 'Иван', 'last_name': 'Иванович'},
    }

.. code-block:: python

    my_dict = {
        'date': '1969-07-21',
        'age': 42,
        'astronaut': {'name': 'Jan Twardowski', 'medals': {'Medal of Honor', 'Purple Heart'}},
        'agency': ['POLSA', 'Roscosmos', 'ESA'],
        'location': ('Baikonur', 'Johnson Space Center'),
    }


``list`` of ``dict``
====================

Getting elements
----------------
.. code-block:: python

    DATA = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

    DATA[0]
    # {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa')

    DATA[0]['measurements']
    # [4.7, 3.2, 1.3, 0.2]

    DATA[0]['measurements'][2]
    # 1.3

    DATA[0]['species']
    # 'setosa'

.. code-block:: python

    DATA = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

    DATA[0].get('kind')
    # KeyError: 'kind'

    DATA[0].get('kind', 'n/a')
    # 'n/a'

    DATA[2].get('measurements')
    # [7.6, 3.0, 6.6, 2.1]

    DATA[2].get('measurements')[1]
    # 3.0

Length
------
.. code-block:: python

    DATA = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

    len(DATA)
    # 3

    len(DATA[0])
    # 2

    len(DATA[1])
    # 2

    len(DATA[1]['species'])
    # 10

    len(DATA[1]['measurements'])
    # 4

Type Annotation
---------------
.. code-block:: python

    from typing import Dict, List


    DATA: List[dict] = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

.. code-block:: python

    from typing import Dict, List, Union


    DATA: List[Dict[str, Union[List[float], str]]] = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]
