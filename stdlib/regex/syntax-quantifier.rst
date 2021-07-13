Regex Quantifier
================


Rationale
---------
Quantifier specifies how many occurrences of preceding qualifier or identifier.


Greedy
------
* Prefer longest matches
* Default

* ``{n}`` - exactly `n` repetitions, prefer longer
* ``{,n}`` - maximum `n` repetitions, prefer longer
* ``{n,}`` - minimum `n` repetitions, prefer longer
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer
* ``*`` - minimum 0 repetitions, no maximum, prefer longer
* ``+`` - minimum 1 repetitions, no maximum, prefer longer
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer


Lazy
----
* Non-greedy
* Prefer shortest matches

* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter


Examples
--------
* ``[0-9]{2}`` - exactly two digits from `0` to `9`
* ``\d{2}`` - exactly two digits from `0` to `9`
* ``[A-Z]{2,10}`` - two to ten uppercase letters from `A` to `Z`
* ``[A-Z]{2-10}-[0-9]{,5}`` - two to ten uppercase letters from `A` to `Z` followed by dash (`-`) and at least five numbers
* ``[a-z]+`` - at least one lowercase letter from `a` to `z`, but try to fit the longest match
* ``\d+`` - number
* ``\d+\.\d+`` - float
