Case Study: Str Concat
======================

Environment:

>>> import sys
>>> import platform
>>>
>>> sys.version_info  # doctest: +SKIP
sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
>>>
>>> platform.platform()  # doctest: +SKIP
'macOS-13.0.1-x86_64-i386-64bit'


SetUp:

>>> firstname = 'Mark'
>>> lastname = 'Watney'


F-string
--------
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... f'{firstname} {lastname}'
...
103 ns ± 11.7 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)


string + string
---------------
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... firstname + ' ' + lastname
...
131 ns ± 15.9 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)


str.format()
------------
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... '{} {}'.format(firstname, lastname)
...
366 ns ± 52.2 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)

>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... '{0} {1}'.format(firstname, lastname)
...
287 ns ± 32.5 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)

>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... '{fname} {lname}'.format(fname=firstname, lname=lastname)
...
712 ns ± 101 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)


%-style
-------
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... '%s %s' % (firstname, lastname)
...
156 ns ± 36.6 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)

>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... '%(fname)s %(lname)s' % {'fname': firstname, 'lname': lastname}
...
614 ns ± 116 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)

