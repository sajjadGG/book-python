********
Keywords
********


``pass``
========
* Avoid error when you don't specify the body of a block

.. code-block:: python
    :caption: Exceptions has all the content needed inherited from ``Exception`` class. You need something to avoid ``IndentationError``

    class MyError(Exception):


    print('hello')
    # IndentationError: expected an indented block

.. code-block:: python

    class MyError(Exception):
        pass


    print('hello')
    # hello


``__file__``
============
.. code-block:: python

    print(__file__)
    # /src/my_file.py

.. code-block:: python

    import os


    BASE_DIR = os.path.dirname(__file__)

    print(f'Working directory: {BASE_DIR}')
    # Working directory: /src

.. code-block:: python

    import os


    BASE_DIR = os.path.dirname(__file__)
    path = os.path.join(BASE_DIR, 'main.py')

    print(f'Executing: {path}')
    # Executing: /src/main.py


``__name__``
============
* Zmienna ``__name__`` pozwala ustalić czy dany plik jest wykonywany czy importowany.
* Jeżeli dany plik jest wykonywany, zmienna ``__name__`` ustawiana jest na ``'__main__'``.
* Jeżeli dany plik jest importowany jako moduł, zmienna ``__name__`` ustawiana jest na nazwę modułu.
* Jest to przydatne na przykład przy testowaniu modułów.

Example 1
---------
* Wypisane na konsoli zostanie ``'hello world!'`` jeżeli dany plik jest uruchamiany z konsoli.
* Powyższy kod nie wykona się natomiast jeżeli plik zaimportujemy jako moduł w innym pliku.

.. code-block:: python

    if __name__ == '__main__':
        print('hello world')

Example 2
---------
* Jeżeli skrypt wywoływany jest z konsoli "z ręki" to uruchom funckję ``run()``
* Jeżeli został zaimportowany, to ten fragment będzie zignorowany
* I trzeba uruchomić funkcję ``run()`` samodzielnie - kontrolowanie

.. code-block:: python

    def run():
        ...

    if __name__ == '__main__':
        run()

Example
-------
.. code-block:: python

    import logging

    log = logging.getLogger(__name__)

