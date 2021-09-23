FuncProg Scope
==============


Rationale
---------
* Values defined in function does not leak out
* Functions has access to global values
* Shadowing is when you define variable with name identical to the one
  from outer scope
* Shadowing in a function is valid only in a function
* After function return, the original value of a shadowed variable
  is restored
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice


Values Leaking
--------------
Values defined in function does not leak out:

>>> def add(a, b=0):
...     c = 1
>>>
>>>
>>> print(a)
Traceback (most recent call last):
NameError: name 'a' is not defined
>>> print(b)
Traceback (most recent call last):
NameError: name 'b' is not defined
>>> print(c)
Traceback (most recent call last):
NameError: name 'c' is not defined
>>>
>>> add(1)
>>>
>>> print(a)
Traceback (most recent call last):
NameError: name 'a' is not defined
>>> print(b)
Traceback (most recent call last):
NameError: name 'b' is not defined
>>> print(c)
Traceback (most recent call last):
NameError: name 'c' is not defined


Outer Scope
-----------
* Functions has access to global values

>>> data = [1, 2, 3]
>>>
>>>
>>> def add():
...     return sum(data)
>>>
>>>
>>> print(data)
[1, 2, 3]
>>>
>>> add()
6
>>>
>>> print(data)
[1, 2, 3]


Shadowing
---------
* Shadowing is when you define variable with name identical to the one
  from outer scope
* Shadowing in a function is valid only in a function
* After function return, the original value of a shadowed variable
  is restored

>>> data = [1, 2, 3]
>>>
>>>
>>> def add():
...     data = [10, 20, 30]  # Shadows name 'data' from outer scope
...     return sum(data)
>>>
>>>
>>> print(data)
[1, 2, 3]
>>>
>>> add()
60
>>>
>>> print(data)
[1, 2, 3]


Global
------
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice

>>> data = [1, 2, 3]
>>>
>>>
>>> def add():
...     global data
...     data = [10, 20, 30]
...     return sum(data)
>>>
>>>
>>> print(data)
[1, 2, 3]
>>>
>>> add()
60
>>>
>>> print(data)
[10 20, 30]


Global Scope
------------
>>> globals()   # doctest: +SKIP
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>}

>>> dir(globals()['__builtins__'])   # doctest: +SKIP
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',
 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError',
 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError',
 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError',
 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError',
 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError',
 '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__',
 '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin',
 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open',
 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed',
 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
 'super', 'tuple', 'type', 'vars', 'zip']

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> globals()  # doctest: +SKIP
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 'firstname': 'Mark',
 'lastname': 'Watney'}


Local Scope
-----------
* Variables defined inside function
* Variables are not available from outside
* If outside the function, will return the same as ``globals()``

>>> locals()  # doctest: +SKIP
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>}

>>> def echo():
...     a = 1
...     print(locals())
>>>
>>>
>>> echo()
{'a': 1}

>>> def echo(a, b=2):
...     c = 3
...     print(locals())
>>>
>>>
>>> echo(1)
{'a': 1, 'b': 2, 'c': 3}


Shadowing Global Scope
----------------------
Shadowing of a global scope is used frequently in Mocks and Stubs.
This way, we can simulate user input. Note that Mocks and Stubs will
stay until the end of a program.

>>> def input(__prompt):
...     return 'Mark Watney'
>>>
>>>
>>> name = input('Type your name: ')
>>> name
'Mark Watney'
>>>
>>> age = input('Type your age: ')
>>> age
'Mark Watney'

To restore default behavior of ``input()`` function use:

>>> input = __builtins__['input']


Assignments
-----------
.. literalinclude:: assignments/funcprog_scope_a.py
    :caption: :download:`Solution <assignments/funcprog_scope_a.py>`
    :end-before: # Solution
