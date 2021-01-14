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


Design
------
.. figure:: ../_img/designpatterns-chainofresponsibility-bad.png
.. figure:: ../_img/designpatterns-chainofresponsibility-flow.png
.. figure:: ../_img/designpatterns-chainofresponsibility-usecase.png


Implementation
--------------
.. literalinclude:: ../_src/designpatterns-chainofresponsibility.py
    :language: python


Assignments
-----------
.. todo:: Create assignments

* Add Encryptor handler
* Make pipeline: authenticator -> logger -> compressor -> encryptor
