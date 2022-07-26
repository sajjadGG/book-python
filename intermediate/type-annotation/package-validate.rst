Type Annotation Validate
========================


MyPy
----
* Type Checking
* http://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

``setup.cfg``

.. code-block:: ini

    [mypy]
    strict_optional = True


PyType
------
* Type Checking
* https://github.com/google/pytype

.. code-block:: console

    $ pip install pytype
    $ pytype -V 3.9 myfile.py


Pyre-check
----------
* Type Checking
