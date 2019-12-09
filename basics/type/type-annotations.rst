**********************
Basic Type Annotations
**********************


.. epigraph::
    Types are not required, and never will be
    -- Guido van Rossum, Python BDFL

.. highlights::
    * Since Python 3.5
    * ``SyntaxError`` in Python before 3.5
    * Sometimes called "type hints"
    * Good IDE will give you hints
    * Types are used extensively in system libraries
    * More and more books and documentations use types
    * To type check use: ``mypy`` or ``pyre-check`` (more in :ref:`cicd-tools`)


Basic types
===========
.. code-block:: python

    value: int = 30
    value: int = -30

.. code-block:: python
    :caption: Type Annotations

    value: float = 13.37

.. code-block:: python

    my_str: str = ''
    my_str: str = 'Jan Twardowski'

.. code-block:: python

    my_var: bool = True
    my_var: bool = False


Types do not enforce checking
=============================
.. highlights::
    * This code will run without any problems
    * Although ``mypy`` or ``pyre-check`` will throw error

.. code-block:: python

    name: int = 'Jan Twardowski'
    age: float = 30
    is_adult: int = True


Why?
====
.. highlights::
    * Good IDE will highlight, incorrect types

.. code-block:: python

    def add_numbers(a: int, b: float) -> int:
        return int(a + b)


    add_numbers(1, 2.5)
    add_numbers('a', 'b')       # Good IDE should highlight the problem here


More advanced topics
====================
.. note::
    The topic will be continued in chapter: :ref:`Type Annotation`
