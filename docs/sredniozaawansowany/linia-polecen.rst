***********************
Parametry linii poleceń
***********************

``argparse``
============

* https://docs.python.org/3/library/argparse.html#the-add-argument-method

.. code-block:: man

    ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

* name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
* action - The basic type of action to be taken when this argument is encountered at the command line.
* nargs - The number of command-line arguments that should be consumed.
* const - A constant value required by some action and nargs selections.
* default - The value produced if the argument is absent from the command line.
* type - The type to which the command-line argument should be converted.
* choices - A container of the allowable values for the argument.
* required - Whether or not the command-line option may be omitted (optionals only).
* help - A brief description of what the argument does.
* metavar - A name for the argument in usage messages.
* dest - The name of the attribute to be added to the object returned by parse_args().

.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--numbers', nargs='*', default=[1, 2.5, 3.0], type=float)
    script_arguments = parser.parse_args()

    print(script_arguments)
    print(script_arguments.numbers)

.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser(
        prog='PROGRAM NAME',
        description='A foo that bars',
        epilog="And that's how you'd foo a bar")

    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum,
                        default=max, help='sum the integers (default: find the max)')

    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('--bar', nargs='+', help='bar help')
    parser.add_argument('--foobar', nargs='*', default=[1, 2, 3], help='BAR!')

    parser.add_argument('--integers', metavar='int', type=int, choices=range(10),
                        nargs='+', help='an integer in the range 0..9')

    parser.add_argument('--baz', nargs='?', type=int, default=42,
                        help='the bar to %(prog)s (default: %(default)s)')

    parser.add_argument('--move', choices=['rock', 'paper', 'scissors'])

    parser.add_argument('--length', default='10', type=int, required=True)
    parser.add_argument('--width', default=10.5, type=int,
                        help='foo the bars before frobbling')

    parser.add_argument('--input', default='input.csv', type=argparse.FileType('r'))
    parser.add_argument('--output', default='output.c', type=argparse.FileType('w'))

    script_arguments = parser.parse_args()
    print(script_arguments)


.. code-block:: python

    try:
       script = parser.parse_args()
    except SystemExit:
        pass

Uruchamianie poleceń
====================

.. code-block:: python

    import subprocess
    import shlex

    cmd = 'ls -la'

    with subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE) as proc:
        ret = proc.stdout.read()
        print(ret)

Timeout dla wykonywania poleceń
===============================

* ``subprocess.run()`` - New in Python 3.5

.. code-block:: python

    import subprocess
    cmd = ['ping', 'www.google.com']

    try:
        subprocess.run(cmd, timeout=5)
    except subprocess.TimeoutExpired:
        print('process ran too long')


Parsowanie i sanityzacja argumentów
===================================

.. code-block:: python

    >>> import shlex
    >>> import subprocess

    >>> command_line = input()
    /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"

    >>> args = shlex.split(command_line)

    >>> print(args)
    ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]

    >>> p = subprocess.Popen(args) # Success!

Przykład
========

.. code-block:: python

    import argparse
    import sys
    import logging
    import warnings


    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='/tmp/input.csv', type=argparse.FileType('r'))

    try:
        parser.parse_args()
    except SystemExit:
        print('Plik niet')
    """


    def read(filename):
        warnings.warn('Ta funkcja niedługo ulegnie zmianie', PendingDeprecationWarning)

        try:
            with open(filename) as file:
                return file.read()
        except FileNotFoundError:
            logging.critical('Plik nie istnieje')
            sys.exit(2)


    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='/tmp/input.csv', type=read)
    args = parser.parse_args()
    print(args)



Zadania kontrolne
=================

Wyliczanie średniej dla parametrów
----------------------------------

:Nazwa skryptu: ``bin/srednia.py``
:Uruchamianie: ``python bin/srednia.py``

:Zadanie 1:
    Zdefiniuj funkcję ``avg()``, która dla dowolnej liczby parametrów zwróci ich średnią arytmetyczną (lub 0 dla 0 parametrów).

:Zadanie 2:
    Dowolna liczba parametrów podanych z linii poleceń.

:Podpowiedź:
    * ``getopt``
    * ``argparse``
    * ``docopt``

:Uruchamianie: ``python bin/srednia.py 5 10 100 32 -90 27.5``
