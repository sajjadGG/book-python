Enum About
==========
* List of finite choices
* Enumerations


Syntax
------
>>> from enum import Enum
>>>
>>>
>>> class Select(Enum):
...     OPTION1 = 1
...     OPTION2 = 2


SetUp
-----
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'


Switch
------
>>> mycolor = Color('#00FF00')
>>>
>>> mycolor
<Color.GREEN: '#00FF00'>
>>>
>>> mycolor.name
'GREEN'
>>>
>>> mycolor.value
'#00FF00'


Comparison
----------
>>> mycolor = Color('#00FF00')
>>>
>>> mycolor is Color.RED
False
>>>
>>> mycolor is Color.GREEN
True


Iteration
---------
>>> for color in Color:
...     print(color)
Color.RED
Color.GREEN
Color.BLUE


Methods
-------
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'
...
...     @classmethod
...     def get_favourite(cls):
...         return cls.RED

>>> Color.get_favourite()
<Color.RED: '#FF0000'>


Use Case - 0x01
---------------
* HTML Colors

>>> class Color(Enum):
...     AQUA = '#00FFFF'
...     BLACK = '#000000'
...     BLUE = '#0000ff'
...     FUCHSIA = '#FF00FF'
...     GRAY = '#808080'
...     GREEN = '#008000'
...     LIME = '#00ff00'
...     MAROON = '#800000'
...     NAVY = '#000080'
...     OLIVE = '#808000'
...     PINK = '#ff1a8c'
...     PURPLE = '#800080'
...     RED = '#ff0000'
...     SILVER = '#C0C0C0'
...     TEAL = '#008080'
...     WHITE = '#ffffff'
...     YELLOW = '#FFFF00'


.. todo:: Assignments
