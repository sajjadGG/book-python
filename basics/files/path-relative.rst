File Path Relative
==================


Rationale
---------
* Python works with both relative and absolute path
* Path is relative to currently running script
* Path separator ``\`` (backslash) is used on Windows
* Path separator ``/`` (slash) is used on ``*nix`` operating systems: Linux,
  macOS, BSD and other POSIX compliant OSes (excluding older versions of Windows)
* In newer Windows versions both ``\`` and ``/`` works the same

Relative paths works the same on Windows and ``*nix`` (Linux, macOS, BSD, etc.).


Current Directory
-----------------
* Path is relative to currently running script
* ``.`` - Current directory

>>> FILE = 'myfile.txt'
>>> FILE = './myfile.txt'

>>> FILE = 'data/myfile.txt'
>>> FILE = './data/myfile.txt'


Upper Directory
---------------
* Path is relative to currently running script
* ``..`` - Parent directory

>>> FILE = '../myfile.txt'
>>> FILE = '../data/myfile.txt'

>>> FILE = '../../myfile.txt'
>>> FILE = '../../data/myfile.txt'


Current Working Directory
-------------------------
* Returns an absolute path to current working directory

>>> from pathlib import Path
>>>
>>>
>>> path = Path.cwd()
>>> print(path)  # doctest: +SKIP
/home/watney/


Good Practices
--------------
* Never hardcode paths, use constant as a file name or file path
* Convention (singular form): ``FILE``, ``FILENAME``, ``FILEPATH``, ``PATH``
* Convention (plural form): ``FILES``, ``FILENAMES``, ``FILEPATHS``, ``PATHS``
* Note, that ``PATH`` is usually used for other purposes (``sys.path`` or
  ``os.getenv('PATH')``)

>>> FILE = 'myfile.txt'

>>> FILES = [
...     'myfile.txt',
...     'myfile.csv',
... ]


Assignments
-----------
.. literalinclude:: assignments/file_path_a.py
    :caption: :download:`Solution <assignments/file_path_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_path_b.py
    :caption: :download:`Solution <assignments/file_path_b.py>`
    :end-before: # Solution
