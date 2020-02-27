.. _OOP Enum:

********
OOP Enum
********


Rationale
=========
* List of finite choices
* Enumerations


Definition
==========
.. code-block:: python
    :caption: Defining ``enum``

    from enum import Enum


    class Color(Enum):
        RED = '#00FF00'
        GREEN = '#00FF00'
        BLUE = '#0000FF'


    my_color = Color.RED

.. code-block:: python
    :caption: Defining ``enum``

    from enum import Enum

    class Status(Enum):
        ALIVE = 'alive'
        DEAD = 'dead'


Accessing names and values
==========================
.. code-block:: python
    :caption: Accessing names and values

    from enum import Enum

    class Color(Enum):
        RED = '#00FF00'
        GREEN = '#00FF00'
        BLUE = '#0000FF'


    print(Color.RED)        # Color.RED
    print(Color.RED.name)   # RED
    print(Color.RED.value)  # '#00FF00'


Iterating over ``Enum``
=======================
.. code-block:: python
    :caption: Iterating over ``Enum``

    from enum import Enum

    class Color(Enum):
        RED = '#00FF00'
        GREEN = '#00FF00'
        BLUE = '#0000FF'

    for color in Color:
        print(color)

    # Color.RED
    # Color.GREEN
    # Color.BLUE


Identity check
==============
.. code-block:: python
    :caption: Identity check

    my_color = Color('#00FF00')     # <Color.GREEN: '#00FF00'>
    my_color is Color.RED           # False
    my_color is Color.GREEN         # True



Use cases
=========
.. code-block:: python
    :caption: ``enum`` - Example usage

    from enum import Enum

    class Permission(Enum):
        READ_WRITE_EXECUTE = 0b111
        READ_WRITE = 0b110
        READ_EXECUTE = 0b101
        READ = 0b100
        WRITE_EXECUTE = 0b011
        WRITE = 0b010
        EXECUTE = 0b001
        NONE = 0b000


.. code-block:: python
    :caption: ``enum`` - Example usage

    from enum import IntEnum

    class IndexDrives(IntEnum):
        """ This enum holds the index value of drive object entrys
        """
        ControlWord = 0x6040
        StatusWord = 0x6041
        OperationMode = 0x6060


Assignments
===========
.. todo:: Create assignments
