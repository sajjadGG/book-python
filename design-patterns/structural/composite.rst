Composite
=========


Rationale
---------
* EN: Composite
* PL: Kompozyt
* Type: object


Use Cases
---------
* Represent a hierarchy of objects
* Groups (and subgroups) objects in Keynote
* Files in a Folder; when you move folder you also move files
* allows you to represent individual entities and groups of entities in the same manner.
* is a structural design pattern that lets you compose objects into a tree.
* is great if you need the option of swapping hierarchical relationships around.
* makes it easier for you to add new kinds of components
* conform to the Single Responsibility Principle in the way that it separates the aggregation of objects from the features of the object.


Problem
-------
.. code-block:: python

    from dataclasses import dataclass, field


    class Shape:
        def render(self) -> None:
            print('Render Shape')


    @dataclass
    class Group:
        __objects: list[Shape|'Group'] = field(default_factory=list)

        def add(self, obj: Shape|'Group') -> None:
            self.__objects.append(obj)

        def render(self) -> None:
            for obj in self.__objects:
                obj.render()


    if __name__ == '__main__':
        group1 = Group()
        group1.add(Shape())  # square
        group1.add(Shape())  # square

        group2 = Group()
        group2.add(Shape())  # circle
        group2.add(Shape())  # circle

        group = Group()
        group.add(group1)
        group.add(group2)
        group.render()


Design
------
.. figure:: img/designpatterns-composite-gof.png


Implementation
--------------
.. figure:: img/designpatterns-composite-usecase.png

.. literalinclude:: ../_src/designpatterns-composite.py
    :language: python


Assignments
-----------
.. literalinclude:: assignments/structural_composite_a.py
    :language: python
