OOP Rationale
=============


Glossary
--------
* Class - blueprint, idea, receipt
* Instance, Object - incarnation, implementation of an idea
* Variables in a class:

    - Field - generic name for a variable in a class
    - Property - fields which typically do not change
    - State - fields which changes frequently
    - Attribute - field, but in Python also a method

>>> data = tuple()
>>> data.append()
Traceback (most recent call last):
AttributeError: 'tuple' object has no attribute 'append'


Value
-----
* Identifier + Scalar = Value

>>> point_x = 1
>>> point_y = 2
>>> point_z = 3
>>>
>>> print(f'Point: x={point_x}, y={point_y}, z={point_z}')
Point: x=1, y=2, z=3


Structure
---------
* Value + Relation = Structure

>>> point = (1, 2, 3)
>>>
>>> print(f'Point: x={point[0]}, y={point[1]}, z={point[2]}')
Point: x=1, y=2, z=3


Data
----
* Structure + Meaning = Data

>>> point = {'x':1, 'y':2, 'z':3}
>>>
>>> print(f'Point: x={point["x"]}, y={point["y"]}, z={point["z"]}')
Point: x=1, y=2, z=3


Information
-----------
* Data + Behavior = Information
* Entity (class, object)

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def set(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def show(self):
...         return f'x={self.x}, y={self.y}, z={self.z}'
>>>
>>>
>>> point = Point()
>>> point.set(x=1, y=2, z=3)
>>>
>>> print(f'Point: {point.show()}')
Point: x=1, y=2, z=3
