******************************
Class Decorator with Functions
******************************


Syntax
======
* ``decorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:
    .. code-block:: python

        @Decorator
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = Decorator(my_function)


Definition
==========
.. code-block:: python

    class Decorator:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)


Usage
=====
.. code-block:: python

    class Decorator:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)


    @Decorator
    def echo(name):
        print(name)


    echo('Mark Watney')
    # Mark Watney


Examples
========
.. code-block:: python
    :caption: Login Check

    class User:
        def __init__(self):
            self.is_authenticated = False

        def login(self, username, password):
            self.is_authenticated = True


    class LoginCheck:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            if user.is_authenticated:
                return self._func(*args, **kwargs)
            else:
                print('Permission Denied')


    @LoginCheck
    def edit_profile():
        print('Editing profile...')


    user = User()

    edit_profile()
    # Permission Denied

    user.login('admin', 'MyVoiceIsMyPassword')

    edit_profile()
    # Editing profile...

.. code-block:: python
    :caption: Dict Cache

    class Cache(dict):
        def __init__(self, func):
            self._func = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            self[key] = self._func(*key)
            return self[key]


    @Cache
    def my_function(a, b):
        return a * b


    my_function(2, 4)           # 8         # Computed
    my_function('hi', 3)        # 'hihihi'  # Computed
    my_function('ha', 3)        # 'hahaha'  # Computed

    my_function('ha', 3)        # 'hahaha'  # Fetched from cache
    my_function('hi', 3)        # 'hihihi'  # Fetched from cache
    my_function(2, 4)           # 8         # Fetched from cache
    my_function(4, 2)           # 8         # Computed


    my_function
    # {
    #   (2, 4): 8,
    #   ('hi ', 3): 'hihihi',
    #   ('ha', 3): 'hahaha',
    #   (4, 2): 8,
    # }


Assignments
===========

Decorator Class Abspath
-----------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/decorator_cls_abspath.py`

:English:
    #. Create function ``print_file(filename: str) -> str`` which prints file content (filename given as an argument)
    #. Create decorator ``ToAbsolutePath``
    #. Decorator converts to absolute path (``path`` + ``filename``), if filename given as an argument is a relative path

:Polish:
    #. Stwórz funkcję ``print_file(filename: str) -> str`` która wyświetla zawartość pliku (nazwa pliku podana jako argument)
    #. Stwórz dekorator ``ToAbsolutePath``
    #. Dekorator zamienia ścieżkę na bezwzględną (``path`` + ``filename``), jeżeli nazwa pliku podana jako argument jest względna

:Hint:
    * ``__file__``
    * ``os.path.dirname()``
    * ``os.path.basename()``
    * ``os.path.join()``

Decorator Class Type Check
--------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/decorator_cls_typecheck.py`

:English:
    .. todo:: English translation

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator - klasę ``CheckTypes``
    #. Dekorator ma sprawdzać typy danych, wszystkich parametrów wchodzących do funkcji
    #. Jeżeli, którykolwiek się nie zgadza, wyrzuć wyjątek ``TypeError``
    #. Wyjątek ma wypisywać:

        * nazwę parametru
        * typ, który parametr ma (nieprawidłowy)
        * typ, który był oczekiwany

:Input:
    .. code-block:: python

        @check_types
        def echo(a: str, b: int, c: int = 0) -> bool:
            print('Function run as expected')
            return bool(a * b)


        echo('a', 2)
        echo('a', 2)
        echo('b', 2)
        echo(a='b', b=2)
        echo(b=2, a='b')
        echo('b', b=2)

:Hint:
    .. code-block:: python

        echo.__annotations__
        # {'a': <class 'str'>, 'return': <class 'bool'>, 'b': <class 'int'>}
