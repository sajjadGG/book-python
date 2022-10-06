Chain of Responsibility
=======================
* EN: Chain of Responsibility
* PL: Łańcuch zobowiązań
* Type: object


Rationale
---------
* Chain of objects
* Create a pipeline of classes with different responsibilities
* Open/Close Principle for adding new handlers

.. figure:: img/designpatterns-chainofresponsibility-usecase.png


Problem
-------
.. figure:: img/designpatterns-chainofresponsibility-problem.png


Pattern
-------


Solution
--------
.. figure:: img/designpatterns-chainofresponsibility-solution.png

.. literalinclude:: src/designpatterns-chainofresponsibility-solution.py
    :language: python


Assignments
-----------
.. todo:: Assignments

* Add Encryptor handler
* Make pipeline: authenticator -> logger -> compressor -> encryptor
