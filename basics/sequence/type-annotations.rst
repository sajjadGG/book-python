****************
Type Annotations
****************


Tuple
=====
.. code-block:: python
    :caption: Generic type annotation

    data: tuple = ()
    data: tuple = tuple()

    data: tuple = ('a', 2, 3.3)

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Tuple

    data: Tuple[int, int, int] = (1, 2, 3)
    data: Tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
    data: Tuple[str, int, float] = ('a', 2, 3.3)


List
====
.. code-block:: python
    :caption: Generic type annotation

    data: list = list()
    data: list = []

    data: list = ['a', 1, 2.2]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import List

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


Frozenset
=========
.. code-block:: python
    :caption: Generic type annotation

    data: frozenset = set()

    data: frozenset = {'a', 1, 2.2}

.. code-block:: python
    :caption: Explicit type annotation

    from typing import FrozenSet

    data: FrozenSet[int] = {1, 2, 3}
    data: FrozenSet[float] = {0.0, 1.1, 2.2}
    data: FrozenSet[str] = {'a', 'b', 'c'}


``list`` of ``tuple``
=====================
.. code-block:: python
    :caption: Generic type annotation

    from typing import List


    data: List[tuple] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import List, Tuple


    data: List[Tuple[float, float, float, float, str]] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import List, Tuple

    Iris = Tuple[float, float, float, float, str]

    data: List[Iris] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]


``list`` of ``list``
====================
.. code-block:: python
    :caption: Generic type annotation

    from typing import List

    data: List[list] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import List

    data: List[List[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

Unions
======
.. code-block:: python
    :caption: Generic type annotation

    from typing import Union


    data: List[Union[list, tuple, set]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Union, List, Tuple, Set


    data: List[Union[List[int], Tuple[int, int, int], Set[int]]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Union, List, Tuple, Set


    Row = Union[List[int], Tuple[int, int, int], Set[int]]

    data: List[Row] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

New Features
============
.. versionadded:: Python 3.9
    :pep:`585` Will be possible to use ``list[int]``, ``set[int]`` etc without importing from ``typing``
