.. _Basic Files Path:

*********
File Path
*********


Rationale
=========
.. highlights::
    * Never hardcode paths (put path directly to open function)
    * Use constant as a file name or file path
    * Naming convention ``FILE``, ``FILENAME``, ``FILEPATH``, ``PATH``
    * Or their respective plural forms for multiple files
    * Note, that ``PATH`` is usually used for other purposes (``sys.path`` or ``os.getenv('PATH')``)
    * Always use raw-strings ``r"..."``
    * Paths on Windows uses ``\``
    * Paths on ``*nix`` uses ``/``
    * ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes
    * In newer Windows versions both ``\`` and ``/`` works


Absolute path
=============
.. highlights::
    * Absolute path on Windows starts with drive letter
    * Absolute path on ``*nix`` starts with root ``/`` dir
    * Absolute path include all entries in the directories hierarchy

.. code-block:: python

    FILE = r'C:\Users\Watney\myfile.txt'

.. code-block:: python

    FILE = r'/tmp/myfile.txt'


Relative path
=============
.. highlights::
    * Path is relative to currently running script
    * ``.`` - Current directory
    * ``..`` - Parent directory

.. code-block:: python

    FILE = r'myfile.txt'
    FILE = r'./myfile.txt'

    FILE = r'tmp/myfile.txt'
    FILE = r'./tmp/myfile.txt'

    FILE = r'../myfile.txt'
    FILE = r'../tmp/myfile.txt'

    FILE = r'../../myfile.txt'
    FILE = r'../../tmp/myfile.txt'


Escaping characters in path
===========================
* ``\\ `` (slash space) - escapes space
* Note escapes are not needed

.. code-block:: python

    FILE = '/tmp/my file.txt'

    with open(FILE) as file:
        print(file.read())

    # Success!

.. code-block:: python

    FILE = r'/tmp/my file.txt'

    with open(FILE) as file:
        print(file.read())

    # Success!


Current script path
===================
* Returns an absolute path to currently running script

.. code-block:: python

    print(__file__)
    # /home/python/myscript.py


Convert relative path to absolute
=================================
* ``os.path.join()`` adds OS dependent directory separator
* ``os.path.dirname()`` gets the absolute path of the argument

.. code-block:: python

    from os.path import dirname, join


    dirname(__file__)
    # /home/python/

    join(dirname(__file__), 'myfile.txt')
    # /home/python/myfile.txt

