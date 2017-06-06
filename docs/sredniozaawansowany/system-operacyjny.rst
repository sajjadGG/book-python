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
