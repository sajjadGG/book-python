***********
Type System
***********


Type inference
==============
* Static Typing (Java, C++, Swift)

    .. code-block:: java

        String name = new String("José Jiménez")

* Dynamic Typing (Python, PHP, Ruby)

    .. code-block:: python

        name = str('José Jiménez')

* Type inference

    .. code-block:: python

        name = 'José Jiménez'


Type Annotations
================

    Types are not required, and never will be
    -- Guido van Rossum, Python BDFL

* Since Python 3.5
* ``SyntaxError`` in Python before 3.5
* Sometimes called "type hints"
* Good IDE will give you hints
* Types are used extensively in system libraries
* More and more books and documentations use types
* To type check use: ``mypy`` or ``pyre-check`` (more in :ref:`cicd-tools`)

Basic types
-----------
.. code-block:: python

    name: str = 'Jan Twardowski'
    age: int = 30
    is_adult: bool = True

Collections
-----------
.. code-block:: python

    my_list: list = list()
    my_set: set = set()
    my_tuple: tuple = tuple()
    my_dict: dict = dict()

.. code-block:: python

    my_list: list = []
    my_set: set = set()
    my_tuple: tuple = ()
    my_dict: dict = {}

.. code-block:: python

    from typing import List, Tuple, Dict, Set


    my_list: List[float] = [5.8, 2.7, 5.1, 1.9]
    my_set: Set[int] = {0, 2, 4}
    my_tuple: Tuple[str] = ('setosa', 'virginica', 'versicolor')
    my_dict: Dict[int, str] = {0: 'setosa', 1: 'virginica': 2: 'versicolor'}

Types do not enforce checking
-----------------------------
* This code will run without any problems
* Although ``mypy`` or ``pyre-check`` will throw error

.. code-block:: python

    name: int = 'Jan Twardowski'
    age: float = 30
    is_adult: int = True

Why?
----
* Good IDE will highlight, incorrect types

.. code-block:: python

    def sum_numbers(a: int, b: float) -> int:
        return int(a + b)


    sumuj_liczby(1, 2.5)
    sumuj_liczby('a', 'b')

More advanced topics
--------------------
.. note:: The topic will be continued in chapter: :ref:`Type Annotation`


Assignments in Polish
=====================
.. todo:: Create Assignments
