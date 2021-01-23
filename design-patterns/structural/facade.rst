Façade
======


Rationale
---------
* EN: Façade
* PL: Fasada
* Type: object


Use Cases
---------
* Provide simple interface to complex system


Problem
-------
* Every time we want to send a push notification to users, we need to follow all steps:

    * connect() -> Connection
    * authenticate(appid, key) -> AuthToken
    * send(AuthToken, message, target)
    * conn.disconnect()

.. literalinclude:: ../_src/designpatterns-facade-problem.py
    :language: python


Design
------


Implementation
--------------
.. figure:: img/designpatterns-facade-usecase.png

.. literalinclude:: ../_src/designpatterns-facade-impl.py
    :language: python


Assignments
-----------
.. todo:: Create assignments

* Clean datetime
* Split name into firstname and lastname
* Example from ``@staticmethod`` chapter
