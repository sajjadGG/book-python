*****************
System Operacyjny
*****************

``os``
======

.. code-block:: python

    import os

    os.path
    os.walk
    os.path.join
    os.path.abspath
    os.path.dirname

.. code-block:: python

    import os

    for element in os.scandir('/etc'):
        print(element.name)

    script = os.path.basename(__file__)
    PWD = os.path.basename(os.getcwd())

    path = os.path.join(PWD, script)

    print(path)


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

    subprocess.Popen()


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
