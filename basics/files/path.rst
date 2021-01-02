File Path
=========

.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)

.. testsetup::

    from shutil import rmtree
    rmtree('/tmp/a', ignore_errors=True)


Rationale
---------
* Python works with both relative and absolute path
* Path separator ``\`` (backslash) is used on Windows
* Path separator ``/`` (slash) is used on ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)
* In newer Windows versions both ``\`` and ``/`` works the same

Absolute path on Windows:

    >>> FILE = r'C:\Users\Watney\myfile.txt'

Absolute path on ``*nix`` (Linux, macOS, BSD, etc.):

    >>> FILE = '/tmp/myfile.txt'

Relative paths works the same on Windows and ``*nix`` (Linux, macOS, BSD, etc.):

    >>> FILE = 'myfile.txt'
    >>> FILE = 'tmp/myfile.txt'
    >>> FILE = '../myfile.txt'


Good Engineering Practices
--------------------------
* Never hardcode paths, use constant as a file name or file path
* Convention (singular form): ``FILE``, ``FILENAME``, ``FILEPATH``, ``PATH``
* Convention (plural form): ``FILES``, ``FILENAMES``, ``FILEPATHS``, ``PATHS``
* Note, that ``PATH`` is usually used for other purposes (``sys.path`` or ``os.getenv('PATH')``)

    >>> FILE = 'myfile.txt'

    >>> FILES = [
    ...     'myfile.txt',
    ...     'myfile.csv']


Raw Strings
-----------
* Always use raw-strings (``r"..."``) for paths
* Escapes does not matters

    >>> print(r'C:\Users\Admin\file.txt')
    C:\Users\Admin\file.txt

    >>> print('C:\\Users\\Admin\\file.txt')
    C:\Users\Admin\file.txt

    >>> print('C:\Users\Admin\file.txt')
    Traceback (most recent call last):
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex i.e. '\U0001F680' which is 🚀 emoticon
* ``s`` is invalid hexadecimal character
* Only valid characters are ``0123456789abcdefABCDEF``

    >>> import string
    >>>
    >>>
    >>> print(string.hexdigits)
    0123456789abcdefABCDEF


Absolute Path
-------------
* Absolute path on Windows starts with drive letter
* Absolute path on ``*nix`` starts with root ``/`` dir
* Absolute path include all entries in the directories hierarchy

    >>> FILE = r'C:\Users\Watney\myfile.txt'

    >>> FILE = r'/tmp/myfile.txt'


Relative Path
-------------
* Path is relative to currently running script
* ``.`` - Current directory
* ``..`` - Parent directory

>>> FILE = r'myfile.txt'
>>> FILE = r'./myfile.txt'

>>> FILE = r'tmp/myfile.txt'
>>> FILE = r'./tmp/myfile.txt'

>>> FILE = r'../myfile.txt'
>>> FILE = r'../tmp/myfile.txt'

>>> FILE = r'../../myfile.txt'
>>> FILE = r'../../tmp/myfile.txt'


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


Exception Handling
------------------
    >>> try:
    ...     file = open('/tmp/myfile.txt')
    ... except FileNotFoundError:
    ...     print('Sorry, file not found')
    ... except PermissionError:
    ...     print('Sorry, not permitted')
    Sorry, file not found


Create Directories
------------------
    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/a').mkdir()

    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/a').mkdir()
    Traceback (most recent call last):
    FileExistsError: [Errno 17] File exists: '/tmp/a'

    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/a').mkdir(exist_ok=True)

    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/a/b/c').mkdir(parents=True, exist_ok=True)


Touch File
----------
    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/myfile.txt').touch()


Exists and is Directory or File
-------------------------------
    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/myfile.txt').exists()
    True

    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/myfile.txt').is_dir()
    False

    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/myfile.txt').is_file()
    True


Delete directory
----------------
Works only with empty directories:

    >>> from pathlib import Path
    >>>
    >>> Path('/tmp/a').rmdir()
    Traceback (most recent call last):
    OSError: [Errno 66] Directory not empty: '/tmp/a'

Remove directories with files:

    >>> from shutil import rmtree
    >>>
    >>> rmtree('/tmp/a', ignore_errors=True)


Current Working Directory
-------------------------
* Returns an absolute path to current working directory

    >>> from pathlib import Path
    >>>
    >>> Path.cwd()  # doctest: +SKIP
    PosixPath('/home/python/')


Convert Relative Path to Absolute
---------------------------------
    >>> from pathlib import Path
    >>>
    >>> Path(Path.cwd(), 'myfile.txt')  # doctest: +SKIP
    PosixPath('/home/python/myfile.txt')


Script Path
-----------
* Returns an absolute path to currently running script

    >>> print(__file__)  # doctest: +SKIP
    /home/python/myscript.py


Assignments
-----------
.. literalinclude:: assignments/file_path_exception.py
    :caption: :download:`Solution <assignments/file_path_exception.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_path_abspath.py
    :caption: :download:`Solution <assignments/file_path_abspath.py>`
    :end-before: # Solution
