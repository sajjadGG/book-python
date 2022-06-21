Tests
=====


Doctests
--------
.. code-block:: console

    $ python3 -m doctest -v tests/*.py


Unit Tests
----------
.. code-block:: console

    $ python3 -m unittest discover -v tests


Test Coverage
-------------
.. code-block:: console

    $ python3 -m coverage run game
    $ python3 -m coverage xml -o .tmp/coverage.xml


Security Analysis
-----------------
.. code-block:: console

    $ python3 -m bandit --format json --output=.tmp/bandit.json --recursive game


Types
-----
.. code-block:: console

    $ python3 -m mypy --ignore-missing-imports game


Style
-----
.. code-block:: console

    $ python3 -m flake8 --doctest --output-file=.tmp/flake8.txt


Lint
----
.. code-block:: console

    $ python3 -m pylint --output-format=parseable --output=.tmp/pylint.txt --disable=C0114,C0115,C0116,E0401,C0103 game

* C0114 - missing-module-docstring
* C0115 - missing-class-docstring
* C0116 - missing-function-docstring
* E0401 - import-error
* C0103 - invalid-name (errors on ``x`` and ``y`` attribute names)
