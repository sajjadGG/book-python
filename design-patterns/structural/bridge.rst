Bridge
======
* EN: Bridge
* PL: Most
* Type: object


Pattern
-------
* Nested hierarchies of classes

.. figure:: img/designpatterns-bridge-pattern.png

.. literalinclude:: uml/designpatterns-bridge-pattern.md
    :language: md


Problem
-------
* Every time you want to add new manufacturers remote control, you need to add two classes of ``ManufacturerRemoteControl`` and ``ManufacturerAdvancedRemoteControl``
* If you add new another type of remote control, such as ``MovieRemoteControl`` you now has to implement three classes

.. code-block:: text

    Basic Remote Control (turnOn, turnOff)
    Advanced Remote Control (setChannel)
    Movie Remote Control (play, pause, rewind)

.. code-block:: text

    RemoteControl
        SonyRemoteControl
        SamsungRemoteControl
        AdvancedRemoteControl
            SonyAdvancedRemoteControl
            SamsungAdvancedRemoteControl

.. figure:: img/designpatterns-bridge-problem.png

.. literalinclude:: uml/designpatterns-bridge-problem.md
    :language: md

.. literalinclude:: src/designpatterns-bridge-problem.py
    :language: python


Solution
--------
* Hierarchy grows in two different directions
* We can split complex hierarchy into two hierarchies which grows independently

.. figure:: img/designpatterns-bridge-solution-1.png
.. figure:: img/designpatterns-bridge-solution-2.png

.. literalinclude:: uml/designpatterns-bridge-solution.md
    :language: md

.. literalinclude:: src/designpatterns-bridge-solution.py
    :language: python


Assignments
-----------
.. todo:: Assignments
