************
C Extensions
************

* biblioteka ``ctypes``
* C Modules

C Types
=======

Kompilacja
----------
.. code:: console

    $ include_dir='-I/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/include/python3.6m/'
    $ gcc -fPIC -c -o mylib-ctypes.o mylib-ctypes.c ${include_dir}
    $ gcc -shared mylib-ctypes.o -o mylib-ctypes.so

Przykład - Rekurencja
---------------------
.. code-block:: C

    long factorial(long n) {
        if (n == 0)
            return 1;

        return (n * factorial(n - 1));
    }

.. code-block:: python

    >>> import ctypes
    >>> lib = ctypes.CDLL('mylib-ctypes.so')

    >>> lib.factorial(16)
    2004189184

    >>> lib.factorial(17)
    -288522240

Argumenty
---------

* ``ctypes.c_double``
* ``ctypes.c_int``
* ``ctypes.c_char``
* ``ctypes.c_char_p``
* ``ctypes.POINTER(ctypes.c_double)``

Przykład - typy proste
----------------------

.. code-block:: C

    #include <stdio.h>

    void ehlo() {
        printf("Ehlo World");
    }

    void greeting(char *name) {
        printf("Ehlo %s!\n", name);
    }

    void number(int num) {
        printf("My number %d\n", num);
    }

    int return_int(int num) {
        return num;
    }

.. code-block:: python

    import ctypes
    lib = ctypes.CDLL('mylib-ctypes.so')

    lib.ehlo()

    lib.greeting.argtypes = [ctypes.c_char_p]
    name = ctypes.create_string_buffer('Matt'.encode())
    lib.greeting(name)

    lib.number(10)

    print(dir(lib))

    i = lib.return_int(15)
    print(i)

Wywołania funkcji
-----------------

.. code-block:: python

    import sys
    import ctypes


    if sys.platform == 'darwin':
       lib = ctypes.CDLL('/usr/lib/libc.dylib')
    elif sys.platform == 'win32':
        lib = ctypes.CDLL('/usr/lib/libc.dll')
    else:
        lib = ctypes.CDLL('/usr/lib/libc.so')


    lib.printf("I'm C printf() function called from Python")

C Modules
=========

Python 3
--------

.. code-block:: C

    #include <Python.h>

    /* Implementation */

    static PyObject* say_hello(PyObject* self, PyObject* args) {
        const char* name;

        if (!PyArg_ParseTuple(args, "s", &name))
            return NULL;

        printf("Hello %s!\n", name);
        Py_RETURN_NONE;
    }

    static PyObject* version(PyObject* self) {
        return Py_BuildValue("s", "Version 1.0");
    }


    /* Python Binding Definitions */

    static PyMethodDef HelloMethods[] = {
         {"say_hello", say_hello, METH_VARARGS, "Greet somebody."},
         {"version"}, (PyCFunction)version, METH_NOARGS, "returns the version"},
         {NULL, NULL, 0, NULL}
    };

    static struct PyModuleDef hello = {
        PyModuleDef_HEAD_INIT,
        "hello",			/* name of module */
        "",					/* module documentation, may be NULL */
        -1,					/* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        HelloMethods
    };

    PyMODINIT_FUNC PyInit_hello(void) {
        return PyModule_Create(&hello);
    }


Python 2
--------

.. code-block:: C

    #include <Python.h>


    /* Implementation */

    static PyObject* say_hello(PyObject* self, PyObject* args) {
        const char* name;

        if (!PyArg_ParseTuple(args, "s", &name))
            return NULL;

        printf("Hello %s!\n", name);
        Py_RETURN_NONE;
    }

    static PyObject* version(PyObject* self) {
        return Py_BuildValue("s", "Version 1.0");
    }


    /* Python Binding Definitions */

    static PyMethodDef HelloMethods[] = {
         {"say_hello", say_hello, METH_VARARGS, "Greet somebody."},
         {"version"}, (PyCFunction)version, METH_NOARGS, "returns the version"},
         {NULL, NULL, 0, NULL}
    };

    PyMODINIT_FUNC inithello(void) {
         (void) Py_InitModule("hello", HelloMethods);
    }


``setup.py``
------------

.. code-block:: python

    import sys
    from distutils.core import setup, Extension

    if sys.version_info >= (3,):
        print('Building for Python 3')
        module = Extension('hello', sources = ['hello-py3.c'])

    elif sys.version_info >= (2,):
        print('Building for Python 2')
        module = Extension('hello', sources=['hello-py2.c'])

    else:
        print('Unsupported Python version')
        sys.exit(1)

    setup(
        name = 'hello',
        version='1.0',
        description = 'Ehlo World!',
        ext_modules = [module])

.. code-block:: console

    $ python setup.py build

    $ cd build/lib*

    $ python

.. code-block:: python

    import hello
    hello.say_hello('José Jiménez')

Zadania kontrolne
=================

C Types
-------
Wykorzystując C Types wyświetl na ekranie datę i czas, za pomocą funkcji zdefiniowanej w C ``<time.h>``

C Modules
---------
Wykorzystując C Modules wyświetl na ekranie datę i czas, za pomocą funkcji zdefiniowanej w C ``<time.h>``
