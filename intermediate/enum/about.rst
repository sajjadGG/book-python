OOP Enum
========


Rationale
---------
* List of finite choices
* Enumerations
* ``Enum``
* ``IntEnum``
* ``Flag``
* ``IntFlag``


Syntax
------
>>> from enum import Enum
>>>
>>>
>>> class Select(Enum):
...     OPTION1 = 1
...     OPTION2 = 2


Example
-------
>>> from enum import Enum
>>>
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'

>>> from enum import Enum
>>>
>>>
>>> class HTTPStatus(Enum):
...     OK = 200
...     CREATED = 201
...     BAD_REQUEST = 400
...     NOT_FOUND = 404
...     INTERNAL_ERROR = 500


Switch
------
>>> from enum import Enum
>>>
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'
>>>
>>>
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


Identity Check
--------------
>>> from enum import Enum
>>>
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'
>>>
>>>
>>> mycolor = Color('#00FF00')
>>>
>>> mycolor is Color.RED
False
>>> mycolor is Color.GREEN
True


Iterating
---------
Iterating over ``Enum``:

>>> from enum import Enum
>>>
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'
>>>
>>>
>>> for color in Color:
...     print(color)
Color.RED
Color.GREEN
Color.BLUE


Pattern Matching
----------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial

.. figure:: img/oop-enum-keycodes.png

Note, keycodes can vary depending on operating system and programming
language used [mskeycodes]_, [jskeycodes]_.

>>> int('0x1B', base=16)
27
>>>
>>> hex(27)
'0x1b'

>>> from enum import Enum
>>>
>>>
>>> class Key(Enum):
...     ESC = 27            # 0x1B
...     ARROW_LEFT = 37     # 0x25
...     ARROW_UP = 38       # 0x26
...     ARROW_RIGHT = 39    # 0x27
...     ARROW_DOWN = 40     # 0x28
>>>
>>>
>>> # doctest: +SKIP
... match keyboard.on_key_press():
...     case Key.ESC:          game.quit()
...     case Key.ARROW_LEFT:   game.move_left()
...     case Key.ARROW_UP:     game.move_up()
...     case Key.ARROW_RIGHT:  game.move_right()
...     case Key.ARROW_DOWN:   game.move_down()
...     case _: raise ValueError(f'Unrecognized key')


Built-in Enum
-------------
>>> from http import HTTPStatus
>>>
>>>
>>> HTTPStatus(200).name
'OK'
>>>
>>> HTTPStatus(404).name
'NOT_FOUND'
>>>
>>> HTTPStatus(500).name
'INTERNAL_SERVER_ERROR'
>>>
>>> HTTPStatus(418).name
'IM_A_TEAPOT'


Use Case - 0x01
---------------
* Dead or Alive

>>> from enum import Enum
>>>
>>>
>>> class Status(Enum):
...     ALIVE = 'alive'
...     DEAD = 'dead'


Use Case - 0x02
---------------
>>> from enum import Enum
>>>
>>>
>>> class Status(Enum):
...     FULL_HEALTH = 100
...     DEAD = 0
>>>
>>>
>>> hit_points = 100
>>> Status(hit_points)
<Status.FULL_HEALTH: 100>
>>>
>>>
>>> hit_points = 0
>>> Status(hit_points)
<Status.DEAD: 0>


Use Case - 0x03
---------------
* Issue Status

>>> from enum import Enum
>>>
>>>
>>> class IssueStatus(Enum):
...     TODO = 'todo'
...     IN_PROGRESS = 'in progress'
...     IN_REVIEW = 'in review'
...     IN_TEST = 'in test'
...     DONE = 'done'
...     REJECTED = 'rejected'


Use Case - 0x04
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


Use Case - 0x05
---------------
>>> from enum import Enum
>>>
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'
>>>
>>>
>>> Point = tuple[int,int]
>>>
>>> def draw_line(A: Point, B: Point, color: Color):
...     if type(color) is not Color:
...         possible = [str(c) for c in Color]
...         raise TypeError(f'Invalid color, possible choices: {possible}')
...     print(f'Drawing line from {A} to {B} with color {color.value}')
>>>
>>>
>>> draw_line(A=(0,0), B=(3,5), color=Color.RED)
Drawing line from (0, 0) to (3, 5) with color #FF0000
>>>
>>> draw_line(A=(0,0), B=(3,5), color='red')
Traceback (most recent call last):
TypeError: Invalid color, possible choices: ['Color.RED', 'Color.GREEN', 'Color.BLUE']


Use Case - 0x06
---------------
* ``r`` - read
* ``w`` - write
* ``x`` - execute
* ``rwx`` - read, write, execute; 0b111 == 0o7
* ``rw-`` - read, write; 0b110 == 0o6
* ``r-x`` - read, execute; 0b101 == 0o5
* ``r--`` - read only; 0b100 == 0o4
* ``rwxr-xr--`` - user=(read,write,execute); group=(read,execute); others=(read)

* https://docs.python.org/3/library/os.html#os.stat

>>> from enum import Enum
>>> from pathlib import Path
>>>
>>>
>>> class Permission(Enum):
...     READ_WRITE_EXECUTE = 0b111
...     READ_WRITE = 0b110
...     READ_EXECUTE = 0b101
...     READ = 0b100
...     WRITE_EXECUTE = 0b011
...     WRITE = 0b010
...     EXECUTE = 0b001
...     NONE = 0b000
>>>
>>>
>>> file = Path('_temporary.txt')
>>> file.touch()
>>> file.stat()  # doctest: +SKIP
os.stat_result(st_mode=33188, st_ino=98480473, st_dev=16777220,
               st_nlink=1, st_uid=501, st_gid=20, st_size=0,
               st_atime=1624458230, st_mtime=1624458230,
               st_ctime=1624458230)
>>>
>>> permissions = file.stat().st_mode
>>> decimal = int(permissions)
>>> octal = oct(permissions)
>>> binary = bin(permissions)
>>> print(f'{decimal=}, {octal=}, {binary}')
decimal=33188, octal='0o100644', 0b1000000110100100
>>>
>>> *_, user, group, others = oct(permissions)
>>> print(f'{user=} {group=} {others=}')
user='6' group='4' others='4'
>>>
>>> Permission(int(user))
<Permission.READ_WRITE: 6>
>>>
>>> Permission(int(group))
<Permission.READ: 4>
>>>
>>> Permission(int(others))
<Permission.READ: 4>
>>>
>>> file.unlink()


Use Case - 0x07
------------------
>>> from enum import IntEnum
>>>
>>>
>>> class IndexDrives(IntEnum):
...     ControlWord = 0x6040
...     StatusWord = 0x6041
...     OperationMode = 0x6060


References
----------
.. [mskeycodes] https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
.. [jskeycodes] https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes


Assignments
-----------
.. todo:: Create assignments
