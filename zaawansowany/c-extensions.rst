************
C Extensions
************

C Types
=======

.. code:: C

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

    int myint(int num) {
        return num;
    }

.. code:: shell

    gcc -fPIC -c -o hello-ctypes.o hello-ctypes.c -I/usr/local/Cellar/python3/3.5.2/Frameworks/Python.framework/Versions/3.5/include/python3.5m/
    gcc -shared hello-ctypes.o -o hello-ctypes.so

.. code-block:: python

    import ctypes

    ehlo = ctypes.CDLL('hello-ctypes.so')

    ehlo.ehlo()

    ehlo.greeting.argtypes = [ctypes.c_char_p]
    name = ctypes.create_string_buffer('Matt'.encode())
    ehlo.greeting(name)

    ehlo.number(10)

    print(dir(ehlo))


    i = ehlo.myint(15)
    print(i)


C Modules
=========

Python 3
--------

.. code:: C

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

.. code:: C

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

.. code:: shell

    python setup.py build
    cd build/lib*
    python

.. code-block:: python

    import hello
    hello.say_hello('Matt')
