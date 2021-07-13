Regex Qualifier
===============


Rationale
---------
Qualifier specifies range to find.



Enumerations
------------
* ``[abc]`` - letter `a` or `b` or `c`


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`


Alternative
-----------
* ``a|b`` - letter `a` or `b` (also works with expressions)
* ``[a-z]|[0-9]`` - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`


Special
-------
* ``?`` - any character
* ``.`` - any character except a newline


Anchors
-------
* ``^`` - start of a string (changes meaning with ``re.MULTILINE``)
* ``$`` - end of a string (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of a string (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of a string (doesn't change meaning with ``re.MULTILINE``)
* ``\G`` - beginning of string or end of previous match


Examples
--------
* ``[d-m]`` - any lowercase letter from `d`  to `m`
* ``[3-7]`` - any digit from `3` to `7`
* ``[d-mK-P3-8]`` - any lowercase letter from `d` to `m` or uppercase letter from `K` to `P` or digit from `3` to `8`
* ``[xz2]`` - `x` or `z` or `2`
* ``x|z|2`` - `x` or `z` or `2`
* ``d|x`` - `d` or `x`
* ``[d-k]|[ABC]|[3-8]`` - any lowercase letter from `d` to `k` or uppercase `A`,`B` or `C` or digit from `3` to `8`
* ``[A-Z][a-z]`` - any capital letter from `A` to `Z` immediately followed by lowercase letter from `a` to `z`
* ``abc.e`` - text `abc` then any character followed by letter `e`
