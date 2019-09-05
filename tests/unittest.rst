************
Unit Testing
************

.. figure:: img/geek-and-poke-development-driven-tests.jpg
    :align: center
    :scale: 12%

    Development driven tests

- https://martinfowler.com/articles/microservice-testing/#testing-component-out-of-process-diagram
- https://docs.python.org/3/library/unittest.mock.html


Glossary
========
.. glossary::

    Stub
        A method stub or simply stub in software development is a piece of code used to stand in for some other programming functionality. A stub may simulate the behavior of existing code (such as a procedure on a remote machine) or be a temporary substitute for yet-to-be-developed code. Stubs are therefore most useful in porting, distributed computing as well as general software development and testing.

    Mock
        In object-oriented programming, mock objects are simulated objects that mimic the behavior of real objects in controlled ways. In a unit test, mock objects can simulate the behavior of complex, real objects and are therefore useful when a real object is impractical or impossible to incorporate into a unit test.

    Unittest
        In computer programming, unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine whether they are fit for use.


Running tests
=============

Running tests with your IDE
---------------------------
* View menu -> Run... -> Unittest in ``my_function``

From code
---------
.. code-block:: python

    if __name__ == "__main__":
        import unittest
        unittest.main()

From command line
-----------------
.. code-block:: console
    :caption: Display only errors

    $ python -m unittest example.py

.. code-block:: console
    :caption: With ``-v`` display progress

    python -m unittest -v example.py


Example
=======

Example 1
---------
.. literalinclude:: src/unittest-example-1.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 2
---------
.. literalinclude:: src/unittest-example-2.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 3
---------
.. literalinclude:: src/unittest-example-3.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 4
---------
.. literalinclude:: src/unittest-example-4.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 5
---------
.. literalinclude:: src/unittest-example-5.py
    :language: python
    :caption: Example ``unittest`` code coverage


Assignments
===========

Dragon
------
* Complexity level: medium
* Lines of code to write: 100 lines
* Estimated time of completion: 25 min

:English:
    #. Write unittest for the dragon created in exam at the end of :ref:`OOP Syntax` chapter

:Polish:
    #. Napisz testy jednostkowe dla Smoka z egzaminu na końcu rozdziału :ref:`OOP Syntax`
