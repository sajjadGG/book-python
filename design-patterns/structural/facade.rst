Façade
======
* EN: Façade
* PL: Fasada
* Type: object


Pattern
-------
* Provide simple interface to complex system

.. figure:: img/designpatterns-facade-pattern.png

.. literalinclude:: uml/designpatterns-facade-pattern.md
    :language: md


Problem
-------
* Every time we want to send a push notification to users, we need to follow all steps:

    * connect() -> Connection
    * authenticate(appid, key) -> AuthToken
    * send(AuthToken, message, target)
    * conn.disconnect()

.. figure:: img/designpatterns-facade-problem.png

.. literalinclude:: uml/designpatterns-facade-problem.md
    :language: md

.. literalinclude:: src/designpatterns-facade-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-facade-solution.png

.. literalinclude:: uml/designpatterns-facade-solution.md
    :language: md

.. literalinclude:: src/designpatterns-facade-solution.py
    :language: python


Assignments
-----------
.. todo:: Assignments

* Clean datetime
* Split name into firstname and lastname
* Example from ``@staticmethod`` chapter
