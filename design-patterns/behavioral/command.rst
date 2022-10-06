Command
=======
* EN: Command
* PL: Polecenie
* Type: object


Rationale
---------
* GUI Buttons, menus
* Macro recording
* Multi level undo/redo (See Tutorial)
* Networking — send whole command objects across a network, even as a batch
* Parallel processing or thread pools
* Transactional behaviour — Rollback whole set of commands, or defer till later
* Wizards

* Source [#medium]_


Problem
-------
.. code-block:: python

.. literalinclude:: src/designpatterns-command-problem.py
    :language: python


Pattern
-------
* Receiver — The Object that will receive and execute the command
* Invoker — Which will send the command to the receiver
* Command Object — Itself, which implements an execute, or action method, and contains all required information
* Client — The main application or module which is aware of the Receiver, Invoker and Commands

.. figure:: img/designpatterns-command-pattern.png


Solution
--------
.. figure:: img/designpatterns-command-usecase.png

Command pattern:

.. literalinclude:: ../_src/designpatterns-command-1.py
    :language: python

Composite commands (Macros):

.. literalinclude:: ../_src/designpatterns-command-2.py
    :language: python

Undoable commands:

.. literalinclude:: ../_src/designpatterns-command-3.py
    :language: python


References
----------
.. [#medium] https://medium.com/design-patterns-in-python/command-design-pattern-in-python-2f15b09f3774



Assignments
-----------
.. todo:: Assignments
