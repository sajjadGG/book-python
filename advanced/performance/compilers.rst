Compilers and Interpreters
==========================
* https://docs.python.org/3/library/py_compile.html
* https://docs.python.org/3/library/compileall.html#module-compileall
* https://docs.python.org/3/library/zipapp.html

Sam Python jest tak naprawdę tylko specyfikacją składni oraz wyglądu
biblioteki standardowej. Python ma obecnie kilka interpreterów z których
najbardziej popularny jest cPython, który jest wydawany razem z nową
wersją specyfikacji języka.


cPython
-------
Domyślną wersją Pythona jest cPython. Jest to tzw. implementacja wzorcowa
i to jej kompilator jest wydawany wraz ze specyfikacją nowych funkcjonalności
przy każdym wydaniu Python. Sam kompilator jest rozwijany w języku C.
cPython jest najbardziej popularną dystrybucją z wszystkich wydań.
W poniższych materiałach to właśnie z tej wersji będziemy korzystać.


Cython
------
* Cython is a compiled language that generates CPython extension modules
* Cython is a superset of the Python programming language
* Designed to give C-like performance with code that is written mostly in Python
* These extension modules can then be loaded and used by regular Python code using the import statement


PyPy
----
Bardzo ciekawy projekt napisania interpretera Pythona w... Pythonie. Kompilator dokonuje bardzo wielu niskopoziomowych optymalizacji dlatego ta wersja języka jest wyjątkowo szybka. Niestety nie wszystkie biblioteki zewnętrzne są z nią kompatybilne. Nie mniej projekt jest wciąż aktywnie rozwijany przez bardzo pomysłowych programistów i stanowi solidną alternatywę dla cPythona. Niektóre programy przy wykorzystaniu PyPy potrafią przyspieszyć kilkuset do kilku tysiąckrotnie.


IronPython
----------
Próba implementacji języka Python wykorzystując platformę .NET firmy Microsoft. Dzięki temu język bardzo dobrze integruje się z całym środowiskiem.


Jython
------
Próba implementacji języka Python wykorzystując platformę wirtualnej maszyny JAVA (JVM). Projekt bardzo obiecujący lecz niestety ostatnio słabo rozwijany. JVM stanowi bardzo dobrą platformę dobrze "wygrzaną" oraz poznaną pod względem wydajnościowym jak i środowiska developerskiego.


Micropython
-----------
* MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.
* MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.
* MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system.
* In addition to implementing a selection of core Python libraries, MicroPython includes modules such as "machine" for accessing low-level hardware.
* https://micropython.org/
* IoT


Pyston
------
* Pyston is an open-source faster implementation of the Python programming language, designed for the performance and compatibility challenges of large real-world applications.
* Pyston was started at Dropbox in 2014 in order to reduce the costs of its rapidly-growing Python server fleet.
* In 2019 the Pyston developers regrouped without a corporate sponsor and started investigating alternative approaches to speeding up Python. They ended up deciding to fork CPython 3.8, and by early 2020 they restarted the project in a new codebase, and called it "Pyston v2". The first version of Pyston v2 was released in late 2020.
* In mid-2021 the Pyston developers joined Anaconda, which since then has provided funding for the project and packaging expertise.
* https://www.pyston.org/
* https://github.com/pyston/pyston


GPython
-------
* gpython is a part re-implementation, part port of the Python 3.4 interpreter in Go.
* https://github.com/go-python/gpython


RustPython
----------
* RustPython is a Python interpreter written in Rust.
* RustPython can be embedded into Rust programs to use Python as a scripting language for your application, or it can be compiled to WebAssembly in order to run Python in the browser.
* RustPython is free and open-source under the MIT license.
* https://rustpython.github.io/


Cinder
------
* Cinder is Meta's (Facebook/Instagram) internal performance-oriented production version of CPython 3.8.
* It contains a number of performance optimizations, including bytecode inline caching, eager evaluation of coroutines, a method-at-a-time JIT, and an experimental bytecode compiler that uses type annotations to emit type-specialized bytecode that performs better in the JIT.
* Cinder is powering Instagram, where it started, and is increasingly used across more and more Python applications in Meta.
* https://github.com/facebookincubator/cinder


PyScript
--------
* framework that allows users to create rich Python applications in the browser using a mix of Python with standard HTML. PyScript aims to give users a first-class programming language that has consistent styling rules, is more expressive, and is easier to learn.
* https://pyscript.net/
* https://github.com/pyscript/pyscript
* https://anaconda.cloud/pyscript-pycon2022-peter-wang-keynote


HPy
---
* HPy provides a new API for extending Python in C.
* In other words, you use #include <hpy.h> instead of #include <Python.h>.
* Zero overhead on CPython: extensions written in HPy runs at the same speed as "normal" extensions.
* Much faster on alternative implementations such as PyPy, GraalPython.
* Debug Mode: in debug mode, you can easily identify common problems such as memory leaks, invalid lifetime of objects, invalid usage of APIs. Have you ever forgot a Py_INCREF or Py_DECREF? The HPy debug mode will detect these mistakes for you.
* Universal binaries: extensions built for the HPy Universal ABI can be loaded unmodified on CPython, PyPy, GraalPython, etc.
* Nicer API: the standard Python/C API shows its age. HPy is designed to overcome some of its limitations, be more consistent, produce better quality extensions and to make it harder to introduce bugs.
* Evolvability: As nicely summarized in [PEP-620](https://peps.python.org/pep-0620/) the standard Python/C API exposes a lot of internal implementation details which makes it hard to evolve the C API. HPy doesn't have this problem because all internal implementation details are hidden.
* https://hpyproject.org/


GraalPython
-----------
* High-Performance. Modern Python
* On average, Python in GraalVM is 8.92x faster than CPython and 8.34x faster than Jython
* GraalVM provides a Python 3.8 compliant runtime.
* A primary goal of the GraalVM Python runtime is to support SciPy and its constituent libraries, as well as to work with other data science and machine learning libraries from the rich Python ecosystem.
* https://www.graalvm.org/python/


Cython
------
* https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

>>> # doctest: +SKIP
... import cython
...
...
... def primes(nb_primes: cython.int):
...     i: cython.int
...     p: cython.int[1000]
...
...     if nb_primes > 1000:
...         nb_primes = 1000
...
...     if not cython.compiled:  # Only if regular Python is running
...         p = [0] * 1000       # Make p work almost like a C array
...
...     len_p: cython.int = 0  # The current number of elements in p.
...     n: cython.int = 2
...     while len_p < nb_primes:
...         # Is n prime?
...         for i in p[:len_p]:
...             if n % i == 0:
...                 break
...
...         # If no break occurred in the loop, we have a prime.
...         else:
...             p[len_p] = n
...             len_p += 1
...         n += 1
...
...     # Let's copy the result into a Python list:
...     result_as_list = [prime for prime in p[:len_p]]
...     return result_as_list


Mypyc
-----
* Mypyc compiles Python modules to C extensions.
* It uses standard Python type hints to generate fast code.
* https://mypyc.readthedocs.io/en/latest/


Nuitka
------
* https://www.nuitka.net

Nuitka is the optimizing Python compiler written in Python that creates
executables that run without an need for a separate installer. Data files
can both be included or put alongside.

It is easy to use and just works. It is fully compatible with Python2
(2.6, 2.7) and Python3 (3.3 - 3.10), works on Windows, macOS, Linux and
more, basically where Python works for you already.

The standard edition bundles your code, dependencies and data into a single
executable if you want. It also does acceleration, just running faster in
the same environment, and can produce extension modules as well. It is
freely distributed under the Apache license.


Others
------
W internecie jest dostępnych jeszcze więcej implementacji języka. Niektóre
projekty są jeszcze rozwijane, niektóre (Stackless Python) weszły w skład
lub transformowały się w wyżej wymienionych lub zostały zarzucone (Unladen
Swallow).


Compiling
---------
* https://py2app.readthedocs.io/
* http://www.py2exe.org/
* http://www.pyinstaller.org/
