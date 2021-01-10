OOP Architecture
================


Boxes and Arrows
----------------
.. figure:: img/uml-class-diagram-1.jpg


UML Class Diagram
-----------------
.. figure:: img/uml-class-diagram-2.png

.. figure:: img/uml-class-diagram-3.png

.. figure:: img/uml-class-diagram-4.png

.. figure:: img/uml-class-diagram-5.png

.. figure:: img/uml-class-diagram-6.png

.. figure:: img/uml-class-diagram-7.png

.. figure:: img/uml-class-diagram-8.jpg

.. figure:: img/uml-class-diagram-9.jpg

.. figure:: img/uml-class-diagram-10.png


Mermaid
-------
* ``mermaid`` - Markdown extension

.. code-block:: md

    ```mermaid
    classDiagram
          Animal <|-- Duck
          Animal <|-- Fish
          Animal <|-- Zebra
          Animal : +int age
          Animal : +String gender
          Animal: +isMammal()
          Animal: +mate()

          class Duck{
              +String beakColor
              +swim()
              +quack()
          }

          class Fish{
              -int sizeInFeet
              -canEat()
          }

          class Zebra{
              +bool is_wild
              +run()
          }
    ```
