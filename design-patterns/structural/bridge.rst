Bridge
======


Rationale
---------
* EN: Bridge
* PL: Most
* Type: object


Use Cases
---------
* Nested hierarchies of classes


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


.. literalinclude:: ../_src/designpatterns-bridge.py
    :language: python


Design
------
.. figure:: ../_img/designpatterns-bridge-usecase1.png
.. figure:: ../_img/designpatterns-bridge-usecase2.png
.. figure:: ../_img/designpatterns-bridge-usecase3.png


Implementation
--------------
* Hierarchy grows in two different directions
* We can split complex hierarchy into two hierarchies which grows independently

.. literalinclude:: ../_src/designpatterns-bridge.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
