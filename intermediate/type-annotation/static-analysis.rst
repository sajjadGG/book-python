Type Annotation Static Analysis
===============================


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



PyAnnotate
----------
* Annotating existing code
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html

The -w flag means "go ahead, update the file":

.. code-block:: console

    $ pip install pyannotate
    $ pyannotate -w myfile.py


Monkeytype
----------
* Annotating existing code
* https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881

.. code-block:: console

    $ pip install monkeytype
    $ monkeytype run runtests.py
    $ monkeytype stub some.module
    $ monkeytype apply some.module
