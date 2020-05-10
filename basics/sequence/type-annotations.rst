****************
Type Annotations
****************

Tuple
=====
.. code-block:: python
    :caption: Generic type annotation

    my_tuple: tuple = ()
    my_tuple: tuple = tuple()

    my_tuple: tuple = ('a', 2, 3.3)

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Tuple

    my_tuple: Tuple[int, int, int] = (1, 2, 3)
    my_tuple: Tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
    my_tuple: Tuple[str, int, float] = ('a', 2, 3.3)


List
====
.. code-block:: python
    :caption: Generic type annotation

    data: list = list()
    data: list = []

    data: list = ['a', 1, 2.2]

.. code-block:: python

    from typing import List
    :caption: Explicit type annotation

    data: List[int] = [1, 2, 3, 4]
    data: List[float] = [5.8, 2.7, 5.1, 1.9]
    data: List[str] = ['a', 'b', 'c', 'd']


Set
===
.. code-block:: python
    :caption: Generic type annotation

    data: set = set()

    data: set = {'a', 1, 2.2}

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Set

    data: Set[int] = {1, 2, 3}
    data: Set[float] = {0.0, 1.1, 2.2}
    data: Set[str] = {'a', 'b', 'c'}


``list`` of ``tuple``
=====================
.. code-block:: python
    :caption: Generic type annotation

    from typing import List


    DATA: List[tuple] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import List, Tuple


    DATA: List[Tuple[float, float, float, float, str]] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]


``list`` of ``list``
====================
.. code-block:: python
    :caption: Generic type annotation

    from typing import List

    DATA: List[list] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import List

    DATA: List[List[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

Unions
======

.. code-block:: python
    :caption: Generic type annotation

    from typing import List


    DATA: List[Union[list, tuple, set]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Set, List, Union, Tuple


    DATA: List[Union[List[int], Tuple[int, int, int], Set[int]]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]
