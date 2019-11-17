.. _Function Type Annotation:

************************
Function Type Annotation
************************


Type annotations
================
.. highlights::
    * Since Python 3.5
    * Types are not forced
    * Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
    * Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów

.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers(1, 2)
    # 3

.. code-block:: python
    :caption: Python will execute without even warning. Your IDE and ``mypy`` will yield errors.

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers('Jan', 'Twardowski')
    # 'JanTwardowski'

.. code-block:: python

    from typing import Union


    def add_numbers(a: Union[int, float], b: Union[int, float]) -> int:
        return int(a + b)

    add_numbers(1, 2)
    # 3

    add_numbers(1.5, 2.5)
    # 4


.. note:: More about this topic at :ref:`Type Annotation`
