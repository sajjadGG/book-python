*********
Profiling
*********


What's that?
============
* A profile is a set of statistics that describes how often and for how long various parts of the program executed

What to measure?
================
* The profiler modules are designed to provide an execution profile for a given program, not for benchmarking purposes (for that, there is timeit for reasonably accurate results). This particularly applies to benchmarking Python code against C code: the profilers introduce overhead for Python code, but not for C-level functions, and so the C code would seem faster than any Python one.

Profiling with IDE
==================
* Profile in PyCharm

Profiling with cProfile
=======================
.. code-block:: python

    import cProfile

    cProfile.run('import re; re.compile("foo|bar")')
    #          216 function calls (209 primitive calls) in 0.000 seconds
    #    Ordered by: standard name
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #         2    0.000    0.000    0.000    0.000 enum.py:284(__call__)
    #         2    0.000    0.000    0.000    0.000 enum.py:526(__new__)
    #         1    0.000    0.000    0.000    0.000 enum.py:836(__and__)
    #         1    0.000    0.000    0.000    0.000 pydev_import_hook.py:16(do_import)
    #         1    0.000    0.000    0.000    0.000 re.py:232(compile)
    #         1    0.000    0.000    0.000    0.000 re.py:271(_compile)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
    #         2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
    #         2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
    #       3/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
    #         1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
    #         3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
    #         7    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
    #        18    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
    #         7    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
    #       3/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
    #         1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
    #         8    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
    #         2    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
    #         6    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
    #         1    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
    #         1    0.000    0.000    0.000    0.000 sre_parse.py:417(_parse_sub)
    #         2    0.000    0.000    0.000    0.000 sre_parse.py:475(_parse)
    #         1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
    #         2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
    #         1    0.000    0.000    0.000    0.000 sre_parse.py:903(fix_flags)
    #         1    0.000    0.000    0.000    0.000 sre_parse.py:919(parse)
    #         1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
    #         1    0.000    0.000    0.000    0.000 {built-in method builtins.__import__}
    #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    #        25    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    #     29/26    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    #         2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
    #         9    0.000    0.000    0.000    0.000 {built-in method builtins.min}
    #         6    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
    #        48    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #         5    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
    #         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

.. csv-table:: cProfile
    :header: "Name", "Description"

    "ncalls", "for the number of calls"
    "tottime", "for the total time spent in the given function (and excluding time made in calls to sub-functions)"
    "percall", "is the quotient of tottime divided by ncalls"
    "cumtime", "is the cumulative time spent in this and all subfunctions (from invocation till exit)"
    "percall", "is the quotient of cumtime divided by primitive calls"
    "filename:lineno(function)", "provides the respective data of each function"

.. csv-table:: cProfile
    :header: "Name", "Description"

    "calls", "call count"
    "cumulative", "cumulative time"
    "cumtime", "cumulative time"
    "file", "file name"
    "filename", "file name"
    "module", "file name"
    "ncalls", "call count"
    "pcalls", "primitive call count"
    "line", "line number"
    "name", "function name"
    "nfl", "name/file/line"
    "stdname", "standard name"
    "time", "internal time"
    "tottime", "internal time"

.. code-block:: console

    python -m cProfile [-o output_file] [-s sort_order] FILE.py
