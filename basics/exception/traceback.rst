Exception Traceback
===================


Rationale
---------
Traceback will help you track down the bug.

    >>> raise RuntimeError
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    RuntimeError

    >>> raise RuntimeError('Huston we have a problem')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    RuntimeError: Huston we have a problem


Traceback Analysis
------------------
* Stacktrace is 8 levels deep, it's not Java's 200 ;)
* Start analysing traceback from bottom-up

    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> apollo13()
    Traceback (most recent call last):
      File "<input>", line 5, in <module>
      File "<input>", line 2, in apollo13
    RuntimeError: Oxygen tank explosion

    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> apollo13()
    Traceback (most recent call last):
      File "/home/watney/myscript.py", line 5, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion

    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> apollo13()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/Applications/PyCharm 2021.1 EAP.app/Contents/helpers/pydev/_pydev_bundle/pydev_umd.py", line 197, in runfile
        pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
      File "/Applications/PyCharm 2021.1 EAP.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
        exec(compile(contents+"\n", file, 'exec'), glob, loc)
      File "/home/watney/myscript.py", line 4, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion


Change Verbosity Level
----------------------
* Change level with ``sys.tracebacklimit``
* From time to time you can have problems somewhere in the middle, but it's rare
* Last lines are the most important, in most cases error is there

    >>> import sys
    >>> sys.tracebacklimit = 2
    >>>
    >>>
    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> apollo13()
    Traceback (most recent call last):
      File "/home/watney/myscript.py", line 4, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion
