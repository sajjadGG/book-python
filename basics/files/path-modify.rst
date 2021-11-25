File Path Modify
================

.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)

.. testsetup::

    from shutil import rmtree
    rmtree('/tmp/a', ignore_errors=True)


Create Directories
------------------
>>> from pathlib import Path
>>>
>>>
>>> path = Path('/tmp/a')
>>> path.mkdir()

>>> from pathlib import Path
>>>
>>>
>>> path = Path('/tmp/a')
>>> path.mkdir()
Traceback (most recent call last):
FileExistsError: [Errno 17] File exists: '/tmp/a'

>>> from pathlib import Path
>>>
>>>
>>> path = Path('/tmp/a')
>>> path.mkdir(exist_ok=True)


Create Directory Hierarchy
--------------------------
>>> from pathlib import Path
>>>
>>>
>>> path = Path('/tmp/a/b/c')
>>> path.mkdir(parents=True, exist_ok=True)


Delete directory
----------------
Works only with empty directories:

>>> from pathlib import Path
>>>
>>>
>>> path = Path('/tmp/a')
>>> path.rmdir()
Traceback (most recent call last):
OSError: [Errno 66] Directory not empty: '/tmp/a'

Remove directories with files:

>>> from shutil import rmtree
>>>
>>>
>>> path = '/tmp/a'
>>> rmtree(path, ignore_errors=True)


Create File
-----------
* Touch creates a file

>>> from pathlib import Path
>>>
>>>
>>> file = Path('/tmp/myfile.txt')
>>> file.touch()


Check If Exists
---------------
>>> from pathlib import Path
>>>
>>>
>>> file = Path('/tmp/myfile.txt')
>>> file.exists()
True


Is File or Dir
--------------
>>> from pathlib import Path
>>>
>>>
>>> file = Path('/tmp/myfile.txt')
>>>
>>> file.is_dir()
False
>>>
>>> file.is_file()
True


Assignments
-----------
.. literalinclude:: assignments/file_path_a.py
    :caption: :download:`Solution <assignments/file_path_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_path_b.py
    :caption: :download:`Solution <assignments/file_path_b.py>`
    :end-before: # Solution
