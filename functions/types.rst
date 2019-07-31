*****
Types
*****


Type annotations
================
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

.. note:: More about this topic at :ref:`Type Annotation`
