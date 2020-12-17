.. _Function Scope:

**************
Function Scope
**************



Rationale
=========
* Functions has access to global values

.. code-block:: python

    def add(a, b=1):
        c = 0


    print(a)
    # Traceback (most recent call last):
    # NameError: name 'a' is not defined
    print(b)
    # Traceback (most recent call last):
    # NameError: name 'b' is not defined
    print(c)
    # Traceback (most recent call last):
    # NameError: name 'c' is not defined

    add(1)

    print(a)
    # Traceback (most recent call last):
    # NameError: name 'a' is not defined
    print(b)
    # Traceback (most recent call last):
    # NameError: name 'b' is not defined
    print(c)
    # Traceback (most recent call last):
    # NameError: name 'c' is not defined


Outer Scope
===========
* Functions has access to global values

.. code-block:: python

    data = [1, 2, 3]


    def add():
        return sum(data)


    add()
    # 6
    print(data)
    # [1, 2, 3]


Shadowing
=========
.. code-block:: python

    data = [1, 2, 3]


    def add():
        data = [10, 20, 30]  # Shadows name 'data' from outer scope
        return sum(data)


    add()
    # 60
    print(data)
    # [1, 2, 3]


Global
======
.. code-block:: python
    :caption: Modify global, BAD PRACTICE!!

    data = [1, 2, 3]


    def add():
        global data
        data = [10, 20, 30]
        return sum(data)


    add()
    # 60
    print(data)
    # [10, 20, 30]


Pure Function
=============
.. code-block:: python

    def add(a, b):
        return a + b


    add(1, 2)
    # 3
    add(1, 2)
    # 3
    add(1, 2)
    # 3


Impure Function
===============
.. code-block:: python

    c = 3


    def add(a, b):
        return a + b + c


    add(1, 2)
    # 6
    add(1, 2)
    # 6
    add(1, 2)
    # 6

    c = 4

    add(1, 2)
    # 7
    add(1, 2)
    # 7
    add(1, 2)
    # 7


Impure to Pure Function
=======================
.. code-block:: python

    c = 3


    def add(a, b, c):
        return a + b + c


    add(1, 2, c)
    # 6
    add(1, 2, c)
    # 6
    add(1, 2, c)
    # 6

    c = 4

    add(1, 2, c)
    # 7
    add(1, 2, c)
    # 7
    add(1, 2, c)
    # 7


Global Scope
============
.. code-block:: python

    globals()
    # {'__name__': '__main__',
    #  '__doc__': None,
    #  '__package__': None,
    #  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
    #  '__spec__': None,
    #  '__annotations__': {},
    #  '__builtins__': <module 'builtins' (built-in)>}

.. code-block:: python

    dir(globals()['__builtins__'])
    # ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError',
    #  'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
    #  'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
    #  'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError',
    #  'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
    #  'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
    #  'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
    #  'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
    #  'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
    #  'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError',
    #  'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
    #  'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
    #  'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
    #  'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__',
    #  '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii',
    #  'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile',
    #  'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
    #  'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help',
    #  'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals',
    #  'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
    #  'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
    #  'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

.. code-block:: python

    firstname = 'Mark'
    lastname = 'Watney'

    globals()
    # {'__name__': '__main__',
    #  '__doc__': None,
    #  '__package__': None,
    #  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
    #  '__spec__': None,
    #  '__annotations__': {},
    #  '__builtins__': <module 'builtins' (built-in)>,
    #  'firstname': 'Mark',
    #  'lastname': 'Watney'}


Local Scope
===========
* Variables defined inside function
* Variables are not available from outside
* If outside the function, will return the same as ``globals()``

.. code-block:: python

    locals()
    # {'__name__': '__main__',
    #  '__doc__': None,
    #  '__package__': None,
    #  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
    #  '__spec__': None,
    #  '__annotations__': {},
    #  '__builtins__': <module 'builtins' (built-in)>}

.. code-block:: python

    def echo():
        a = 1
        print(locals())


    echo()
    # {'a': 1}

.. code-block:: python

    def echo(a, b=2):
        c = 3
        print(locals())


    echo(1)
    # {'a':1, 'b':2, 'c':3}


Assignments
===========

.. literalinclude:: assignments/function_scope_global.py
    :caption: :download:`Solution <assignments/function_scope_global.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_scope_romanint.py
    :caption: :download:`Solution <assignments/function_scope_romanint.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_scope_introman.py
    :caption: :download:`Solution <assignments/function_scope_introman.py>`
    :end-before: # Solution
