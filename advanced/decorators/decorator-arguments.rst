************************
Decorator with Arguments
************************


Syntax
======
Decorator:
    .. code-block:: python

        @decorator(a, b)
        def function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        decorator = decorator(a, b)(function)


Definition
==========
.. code-block:: python

    def decorator(a=1, b=2):
        def function_wrapper(function):

            def args_wrapper(*args, **kwargs):
                return function(*args, **kwargs)
            return args_wrapper

        return function_wrapper

Usage
=====
.. code-block:: python

    def decorator(a=1, b=2):
        def function_wrapper(function):

            def args_wrapper(*args, **kwargs):
                return function(*args, **kwargs)
            return args_wrapper

        return function_wrapper


    @decorator(a=0)
    def echo(name):
        print(name)


    echo('Mark Watney')
    # Mark Watney


Examples
========

Deprecated
----------
.. code-block:: python

    def deprecated(removed_in_version=None):
        def decorator(fn):
            def write_message(*args, **kwargs):
                name = fn.__name__
                file = fn.__code__.co_filename
                line = fn.__code__.co_firstlineno + 1
                message = f"Call to deprecated function {name} in {file} at line {line}"
                message += f'\nIt will be removed in {removed_in_version}'

                import warnings
                warnings.warn(message, DeprecationWarning)
                return fn(*args, **kwargs)

            return write_message
        return decorator


    @deprecated(removed_in_version=2.0)
    def my_function():
        pass


    my_function()
    # /tmp/my_script.py:11: DeprecationWarning: Call to deprecated function my_function in /tmp/my_script.py at line 19
    # It will be removed in 2.0

Timeout
-------
.. code-block:: python
    :caption: Decorator usage

    from signal import signal, alarm, SIGALRM
    from time import sleep


    def timeout(seconds=2.0, error_message='Timeout'):
        def on_timeout(signum, frame):
            raise TimeoutError

        def decorator(func):
            def wrapper(*args, **kwargs):
                signal(SIGALRM, on_timeout)
                alarm(int(seconds))

                try:
                    func(*args, **kwargs)
                except TimeoutError:
                    print(error_message)
                finally:
                    alarm(0)

            return wrapper
        return decorator


    @timeout(seconds=3.0, error_message='Sorry, timeout')
    def countdown(n):
        for i in reversed(range(n)):
            print(i)
            sleep(1)
        print('countdown finished')


    if __name__ == '__main__':
        countdown(5)
    # 4
    # 3
    # 2
    # Sorry, timeout


.. code-block:: python

    from _thread import interrupt_main
    from threading import Timer
    from time import sleep


    def timeout(seconds=3.0, error_message='Timeout'):
        def decorator(func):
            def wrapper(*args, **kwargs):
                timer = Timer(seconds, interrupt_main)
                timer.start()
                try:
                    result = func(*args, **kwargs)
                except KeyboardInterrupt:
                    raise TimeoutError(error_message)
                finally:
                    timer.cancel()
                return result
            return wrapper
        return decorator


    @timeout(seconds=3.0, error_message='Sorry, timeout')
    def countdown(n):
        for i in reversed(range(n)):
            print(i)
            sleep(1)
        print('countdown finished')


    if __name__ == '__main__':
        countdown(5)
    # 4
    # 3
    # 2
    # TimeoutError: Timeout
