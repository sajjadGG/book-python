Proxy
=====


Rationale
---------
* EN: Proxy
* PL: Pełnomocnik
* Type: object


Use Cases
---------
* Create a proxy, or agent for a remote object
* Agent takes message and forwards to remote object
* Proxy can log, authenticate or cache messages

.. figure:: ../_img/designpatterns-proxy-about.png


Problem
-------
* Creating Ebook object is costly, because we have to read it from the disk and store it in memory
* It will load all ebooks in our library, just to select one

.. literalinclude:: ../_src/designpatterns-proxy-problem.py
    :language: python


Design
------
.. figure:: ../_img/designpatterns-proxy-gof.png


Implementation
--------------
* Lazy evaluation
* Open/Close Principle

.. figure:: ../_img/designpatterns-proxy-usecase.png

.. literalinclude:: ../_src/designpatterns-proxy-impl-1.py
    :language: python

Proxy with Authorization and Logging:

.. literalinclude:: ../_src/designpatterns-proxy-impl-2.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
