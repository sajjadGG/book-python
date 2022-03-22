File Path Absolute
==================
* Python works with both relative and absolute path
* Path separator ``\`` (backslash) is used on Windows
* Path separator ``/`` (slash) is used on ``*nix`` operating systems: Linux,
  macOS, BSD and other POSIX compliant OSes (excluding older versions of Windows)
* In newer Windows versions both ``\`` and ``/`` works the same


Absolute Path
-------------
* Absolute path on Windows starts with drive letter
* Absolute path on ``*nix`` starts with root ``/`` dir
* Absolute path include all entries in the directories hierarchy

>>> FILE = r'C:\Users\Watney\myfile.txt'

>>> FILE = r'/tmp/myfile.txt'


Escaping Characters in Path
---------------------------
* "\\ " (backslash space) - escapes space
* Note that in Python escapes in paths are not required

>>> FILE = '/tmp/my file.txt'

>>> FILE = r'/tmp/my file.txt'

>>> FILE = r'C:\Users\Admin\myfile.txt'
>>>
>>>
>>> repr(FILE)
"'C:\\\\Users\\\\Admin\\\\myfile.txt'"
>>>
>>> str(FILE)
'C:\\Users\\Admin\\myfile.txt'
>>>
>>> print(repr(FILE))
'C:\\Users\\Admin\\myfile.txt'
>>>
>>> print(FILE)
C:\Users\Admin\myfile.txt


Convert Relative Path to Absolute
---------------------------------
>>> from pathlib import Path
>>>
>>>
>>> file = Path('myfile.txt')
>>> file.absolute()  # doctest: +SKIP
/home/watney/myfile.txt


Dirname, Filename
-----------------
>>> from pathlib import Path
>>>
>>>
>>> file = Path('/home/watney/myfile.py')
>>>
>>> print(file.parent)
/home/watney
>>>
>>> print(file.name)
myfile.py


Script Path
-----------
* ``__file__`` - Returns an absolute path to currently running script

>>> print(__file__)  # doctest: +SKIP
/home/watney/myscript.py

>>> from pathlib import Path
>>>
>>>
>>> file = Path(__file__)  # doctest: +SKIP
>>>
>>> print(file.parent)  # doctest: +SKIP
/home/watney
>>>
>>> print(file.name)  # doctest: +SKIP
myfile.py


Assignments
-----------
.. literalinclude:: assignments/file_path_a.py
    :caption: :download:`Solution <assignments/file_path_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_path_b.py
    :caption: :download:`Solution <assignments/file_path_b.py>`
    :end-before: # Solution
