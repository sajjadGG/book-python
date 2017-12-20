\usepackage{ulem}

\usepackage{ulem}

\usepackage{ulem}

*****************
System Operacyjny
*****************

``os``
======

Najczęściej wykorzystuje się:

.. code-block:: python

    import os

    os.walk()
    os.scandir()
    os.getcwd()

    os.path.join()
    os.path.abspath()
    os.path.dirname()
    os.path.basename()

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

Najczęściej wykorzystuje się:

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

Najczęściej wykorzystuje się:

.. code-block:: python

    import subprocess

    subprocess.call('clear')
    subprocess.Popen()
    subprocess.run()


``subprocess.Popen()``
----------------------
.. code-block:: python

    subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True,  shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None)

``subprocess.run()``
--------------------

* New in Python 3.5

.. code-block:: python

    subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)

``shell=True``
--------------

.. code-block:: python

    >>> import subprocess

    >>> subprocess.call('echo $HOME')
    Traceback (most recent call last):
    ...
    OSError: [Errno 2] No such file or directory


    >>> import subprocess
    >>> subprocess.call('echo $HOME', shell=True)
    /home/jose-jimenez
    0

Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process, and tell it to run the command. In other words, using an intermediate shell means that variables, glob patterns, and other special shell features in the command string are processed before the command is run. Here, in the example, ``$HOME`` was processed before the echo command. Actually, this is the case of command with shell expansion while the command ``ls -l`` considered as a simple command.

.. note:: source: `Subprocess Module <https://stackoverflow.com/a/36299483/228517>`


Uruchamianie poleceń
--------------------

.. code-block:: python

    >>> subprocess.run(["ls", "-l"])  # doesn't capture output
    CompletedProcess(args=['ls', '-l'], returncode=0)

    >>> subprocess.run("exit 1", shell=True, check=True)
    Traceback (most recent call last):
      ...
    subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

    >>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
    CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
    stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')

.. code-block:: python

    import subprocess
    import shlex

    cmd = 'ls -la'

    with subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE) as proc:
        ret = proc.stdout.read()
        print(ret)

Timeout dla wykonywania poleceń
-------------------------------

.. code-block:: python

    import subprocess
    cmd = ['ping', 'nasa.gov']

    try:
        subprocess.run(cmd, timeout=5)
    except subprocess.TimeoutExpired:
        print('process ran too long')

Przechwytywanie outputu
-----------------------

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

Rekursywne przechodzenie i wykonywanie poleceń
----------------------------------------------
#. Napisz skrypt, który przeszuka rekurencyjnie wszystkie katalogi na pulpicie w Twoim systemie operacyjnym i jeżeli znajdzie plik *README* (z dowolnym rozszerzeinem) to wyświetli jego zawartość za pomocą polecenia ``cat`` (macOS, Linux) lub ``type`` (Windows).
#. Ścieżkę do pliku ``README`` skonstruuj za pomocją ``os.path.join()``
#. Jeżeli skrypt nie znajdzie pliku README, to ma rzucić informację ``logging.critical()`` i wyjść z kodem błędu ``1``.

:Podpowiedź:
    * Gdyby był problem ze znalezieniem pliku, a ścieżka jest poprawna to zastosuj ``shell=True``
    * ``os.walk()``
    * ``subprocess.run()``

:Co to zadanie sprawdza?:
    * Przeglądanie katalogów i algorytm przeszykiwania
    * Sanityzacja parametrów
    * Logowanie wydarzeń w programie
    * Uruchamianie poleceń w systemie
    * Przechwytywanie outputu poleceń
    * Kody błędów
    * Przechodzenie do katalogów
    * Ścieżki względne i bezwzględne
    * Łączenie ścieżek

Tree
----
Za pomocą znaków unicode: "┣━", "┗━" , "┃  " wygeneruj wynik przypominający wynik polecenia ``tree``.


.. code-block:: text

    root:.
    [.]
    ┣━[.idea]
    ┃  ┣━[scopes]
    ┃  ┃  ┗━scope_settings.xml
    ┃  ┣━.name
    ┃  ┣━Demo.iml
    ┃  ┣━encodings.xml
    ┃  ┣━misc.xml
    ┃  ┣━modules.xml
    ┃  ┣━vcs.xml
    ┃  ┗━workspace.xml
    ┣━[test1]
    ┃  ┗━test1.txt
    ┣━[test2]
    ┃  ┣━[test2-2]
    ┃  ┃  ┗━[test2-3]
    ┃  ┃      ┣━test2
    ┃  ┃      ┗━test2-3-1
    ┃  ┗━test2
    ┣━folder_tree_maker.py
    ┗━tree.py
