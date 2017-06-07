*****************
System Operacyjny
*****************

``os``
======

.. code-block:: python

    import os

    os.path
    os.walk()
    os.scandir()

    os.path.join
    os.path.abspath
    os.path.dirname

    os.remove()
    os.rmdir()

.. code-block:: python

    import os

    for element in os.scandir('/etc'):
        print(element.name)

    script = os.path.basename(__file__)
    PWD = os.path.basename(os.getcwd())

    path = os.path.join(PWD, script)

    print(path)

.. code-block:: python

    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end=" ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

.. code-block:: python

    # Delete everything reachable from the directory named in "top",
    # assuming there are no symbolic links.
    # CAUTION:  This is dangerous!  For example, if top == '/', it
    # could delete all your disk files.
    import os
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


``sys``
=======

.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.platform

.. code-block:: python

    import sys

    sys.exit(0)


``subprocess``
==============

.. code-block:: python

    import subprocess

    subprocess.call('clear')
    subprocess.Popen()
    subprocess.run()


Uruchamianie poleceń
--------------------

.. code-block:: python

    import subprocess
    import shlex

    cmd = 'ls -la'

    with subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE) as proc:
        ret = proc.stdout.read()
        print(ret)

Timeout dla wykonywania poleceń
-------------------------------

* ``subprocess.run()`` - New in Python 3.5

.. code-block:: python

    import subprocess
    cmd = ['ping', 'www.google.com']

    try:
        subprocess.run(cmd, timeout=5)
    except subprocess.TimeoutExpired:
        print('process ran too long')

.. code-block:: python

    def run(command, timeout=15, clear=True):
        if clear:
            subprocess.call('clear')
        log.debug(f'Execute: {command}\n')
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            timeout=timeout,
            encoding='utf-8')
        if result.stdout:
            log.info(f'\n\n{result.stdout}')
        if result.stderr:
            log.warning(f'\n\n{result.stderr}')
        return result


Parsowanie i sanityzacja argumentów
-----------------------------------

.. code-block:: python

    >>> import shlex
    >>> import subprocess

    >>> command_line = input()
    /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"

    >>> args = shlex.split(command_line)

    >>> print(args)
    ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]

    >>> p = subprocess.Popen(args) # Success!


``tempfile``
============

.. code-block:: python

    >>> import tempfile

    # create a temporary file and write some data to it
    >>> fp = tempfile.TemporaryFile()
    >>> fp.write(b'Hello world!')
    # read data from file
    >>> fp.seek(0)
    >>> fp.read()
    b'Hello world!'
    # close the file, it will be removed
    >>> fp.close()

    # create a temporary file using a context manager
    >>> with tempfile.TemporaryFile() as fp:
    ...     fp.write(b'Hello world!')
    ...     fp.seek(0)
    ...     fp.read()
    b'Hello world!'
    >>>
    # file is now closed and removed

    # create a temporary directory using the context manager
    >>> with tempfile.TemporaryDirectory() as tmpdirname:
    ...     print('created temporary directory', tmpdirname)
    >>>
    # directory and contents have been removed

``eval``
========

.. code-block:: python

    >>> x = 1
    >>> eval('x+1')
    2

Zadanie kontrolne
=================

Napisz skrypt, który przeszuka rekurencyjnie wszystkie katalogi na pulpicie w Twoim systemie operacyjnym i jeżeli znajdzie plik README (z dowolnym rozszerzeinem) to wyświetli jego zawartość za pomocą polecenia ``cat`` (macOS, Linux) lub ``type`` (Windows).

Jeżeli skrypt nie znajdzie pliku README, to ma wyjść z kodem błędu
