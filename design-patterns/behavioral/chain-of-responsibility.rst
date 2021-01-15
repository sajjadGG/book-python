Chain of Responsibility
=======================


Rationale
---------
* EN: Chain of Responsibility
* PL: Łańcuch zobowiązań
* Type: object


Use Cases
---------
* Chain of objects
* Create a pipeline of classes with different responsibilities
* Open/Close Principle for adding new handlers

.. figure:: ../_img/designpatterns-chainofresponsibility-flow.png


Problem
-------
.. figure:: ../_img/designpatterns-chainofresponsibility-problem.png


Design
------


Implementation
--------------
.. figure:: ../_img/designpatterns-chainofresponsibility-usecase.png

.. literalinclude:: ../_src/designpatterns-chainofresponsibility.py
    :language: python


Assignments
-----------
.. todo:: Create assignments

* Add Encryptor handler
* Make pipeline: authenticator -> logger -> compressor -> encryptor
