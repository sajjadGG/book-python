**********************
Basic Type Annotations
**********************


.. epigraph::
    Types are not required, and never will be
    -- Guido van Rossum, Python BDFL

Rationale
=========
.. highlights::
    * Since Python 3.5
    * ``SyntaxError`` in Python before 3.5
    * Also known as "type hints"
    * Good IDE will give you hints
    * Types are used extensively in system libraries
    * More and more books and documentations use types
    * To type check use: ``mypy`` or ``pyre-check`` (more in :ref:`cicd-tools`)


Int
===
.. code-block:: python

    data: int = 30
    data: int = -30


Float
=====
.. code-block:: python

    data: float = 13.37
    data: float = -13.37


Str
===
.. code-block:: python

    data: str = ''
    data: str = 'Jan Twardowski'


Bool
====
.. code-block:: python

    data: bool = True
    data: bool = False


Optional
========
.. code-block:: python

    from typing import Optional


    firstname: str = 'Melissa'
    lastname: str = 'Lewis'
    age: Optional[float] = None


Type Check is not Enforced
==========================
.. highlights::
    * This code will run without any problems
    * Although ``mypy`` or ``pyre-check`` will throw error

.. code-block:: python

    name: int = 'Jan Twardowski'
    age: float = 30
    is_adult: int = True


More Advanced Topics
====================
.. note::
    The topic will be continued in chapter: :ref:`Type Annotation`
