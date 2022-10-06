Chain of Responsibility
=======================
* EN: Chain of Responsibility
* PL: Łańcuch zobowiązań
* Type: object


Pattern
-------
* Chain of objects
* Create a pipeline of classes with different responsibilities
* Open/Close Principle for adding new handlers

.. figure:: img/designpatterns-chainofresponsibility-pattern.png

.. literalinclude:: uml/designpatterns-chainofresponsibility-pattern.md
    :language: md


Problem
-------
.. figure:: img/designpatterns-chainofresponsibility-problem.png

.. literalinclude:: uml/designpatterns-chainofresponsibility-problem.md
    :language: md

.. literalinclude:: src/designpatterns-chainofresponsibility-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-chainofresponsibility-solution.png

.. literalinclude:: uml/designpatterns-chainofresponsibility-solution.md
    :language: md

.. literalinclude:: src/designpatterns-chainofresponsibility-solution.py
    :language: python


Assignments
-----------
.. todo:: Assignments

* Add Encryptor handler
* Make pipeline: authenticator -> logger -> compressor -> encryptor
