Block Match
===========
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial
* Significantly faster for sequences and mappings [#Shaw2022]_
* Since Python 3.11: For sequences if faster around 80% [#Shaw2022]_
* Since Python 3.11: For mappings if faster around 80% [#Shaw2022]_

>>> choice = 'r'
>>>
>>> if choice == 'r':
...     color = 'red'
... elif choice == 'g':
...     color = 'green'
... elif choice == 'b':
...     color = 'blue'
... else:
...     color = None

We can use less PEP-8 compliant style, but in this case it increases
readability.

>>> choice = 'r'
>>>
>>> if choice == 'r':    color = 'red'
... elif choice == 'g':  color = 'green'
... elif choice == 'b':  color = 'blue'
... else:                color = None

New ``match`` syntax allows to be ``PEP-8`` compliant while having
clear syntax without condition repetitions:

>>> choice = 'r'
>>>
>>> match choice:
...     case 'r': color = 'red'
...     case 'g': color = 'green'
...     case 'b': color = 'blue'
...     case _:   color = None


Syntax
------
>>> # doctest: +SKIP
... match <object>:
...     case <option>: <action>
...     case <option>: <action>
...     case <option>: <action>
...     case _: <default action>


Patterns
--------
* literal pattern
* capture pattern
* wildcard pattern
* constant value pattern
* sequence pattern
* mapping pattern
* class pattern
* OR pattern
* walrus pattern
* Patterns don't just have to be literals.

The patterns can also:

* Use variable names that are set if a ``case`` matches
* Match sequences using list or tuple syntax (like Python's existing ``iterable unpacking`` feature)
* Match mappings using ``dict`` syntax
* Use ``*`` to match the rest of a list
* Use ``**`` to match other keys in a dict
* Match objects and their attributes using class syntax
* Include "or" patterns with ``|``
* Capture sub-patterns with ``as``
* Include an ``if`` "guard" clause


Literal pattern
---------------
A `literal pattern` is useful to filter constant values in a
structure. It looks like a Python literal (including some values like
``True``, ``False`` and ``None``). It only matches objects equal to
the literal, and never binds.

>>> def html_color(name):
...     match name:
...         case 'red':   return '#ff0000'
...         case 'green': return '#00ff00'
...         case 'blue':  return '#0000ff'
>>>
>>>
>>> html_color('red')
'#ff0000'
>>>
>>> html_color('green')
'#00ff00'
>>>
>>> html_color('blue')
'#0000ff'

>>> def status(result):
...     match result:
...         case True:  return 'success'
...         case False: return 'error'
...         case None:  return 'in-progress'
>>>
>>>
>>> status(True)
'success'
>>>
>>> status(False)
'error'
>>>
>>> status(None)
'in-progress'

>>> def count(*args):
...     match len(args):
...         case 3: return 'Three'
...         case 2: return 'Two'
...         case 1: return 'One'
...         case 0: return 'Too few'
...         case _: return 'Too many'
>>>
>>>
>>> count(1,2,3,4)
'Too many'
>>>
>>> count(1,2,3)
'Three'
>>>
>>> count(1,2)
'Two'
>>>
>>> count(1)
'One'
>>>
>>> count()
'Too few'


Capture pattern
---------------
A `capture pattern` looks like x and is equivalent to an identical
assignment target: it always matches and binds the variable with the
given (simple) name.

>>> class Astronaut:
...     def move_left(self, value):
...         print(f'Moving left by {value}')
...
...     def move_right(self, value):
...         print(f'Moving right by {value}')
...
...     def move_up(self, value):
...         print(f'Moving up by {value}')
...
...     def move_down(self, value):
...         print(f'Moving down by {value}')
>>>
>>>
>>> hero = Astronaut()
>>>
>>> def move(*how):
...     match how:
...         case ['left', value]:   hero.move_left(value)
...         case ['right', value]:  hero.move_right(value)
...         case ['up', value]:     hero.move_up(value)
...         case ['down', value]:   hero.move_down(value)
>>>
>>>
>>> move('left', 1)
Moving left by 1
>>>
>>> move('right', 2)
Moving right by 2
>>>
>>> move('up', 3)
Moving up by 3
>>>
>>> move('down', 4)
Moving down by 4

>>> def _get(path):
...     print(f'Processing GET request for {path}')
>>>
>>> def _post(path):
...     print(f'Processing POST request for {path}')
>>>
>>> def _put(path):
...     print(f'Processing PUT request for {path}')
>>>
>>> def _delete(path):
...     print(f'Processing DELETE request for {path}')
>>>
>>>
>>> def process_request(request):
...     match request.split():
...         case ['GET',    path, 'HTTP/2.0']: _get(path)
...         case ['POST',   path, 'HTTP/2.0']: _post(path)
...         case ['PUT',    path, 'HTTP/2.0']: _put(path)
...         case ['DELETE', path, 'HTTP/2.0']: _delete(path)
>>>
>>>
>>> process_request('POST /user/ HTTP/2.0')
Processing POST request for /user/
>>>
>>> process_request('GET /user/mwatney/ HTTP/2.0')
Processing GET request for /user/mwatney/
>>>
>>> process_request('PUT /user/mwatney/ HTTP/2.0')
Processing PUT request for /user/mwatney/
>>>
>>> process_request('DELETE /user/mwatney/ HTTP/2.0')
Processing DELETE request for /user/mwatney/


Wildcard pattern
----------------
The `wildcard pattern` is a single underscore: ``_``.  It always
matches, but does not capture any variable (which prevents
interference with other uses for ``_`` and allows for some
optimizations).

>>> def html_color(name):
...     match name:
...         case 'red':   return '#ff0000'
...         case 'green': return '#00ff00'
...         case 'blue':  return '#0000ff'
...         case _:       raise NotImplementedError


Constant value pattern
----------------------
A `constant value pattern` works like the literal but for certain named
constants. Note that it must be a qualified (dotted) name, given the
possible ambiguity with a capture pattern. It looks like ``Color.RED``
and only matches values equal to the corresponding value. It never
binds.


Sequence pattern
----------------
A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
list unpacking. An important difference is that the elements nested
within it can be any kind of patterns, not just names or sequences. It
matches only sequences of appropriate length, as long as all the
sub-patterns also match. It makes all the bindings of its sub-patterns.


Mapping pattern
---------------
A `mapping pattern` looks like ``{"user": u, "emails": [*es]}``. It
matches mappings with at least the set of provided keys, and if all the
sub-patterns match their corresponding values. It binds whatever the
sub-patterns bind while matching with the values corresponding to the
keys. Adding **rest at the end of the pattern to capture extra items
is allowed.


Class pattern
-------------
A `class pattern` is similar to the above but matches attributes
instead of keys. It looks like ``datetime.date(year=y, day=d)``. It
matches instances of the given type, having at least the specified
attributes, as long as the attributes match with the corresponding
sub-patterns. It binds whatever the sub-patterns bind when matching
with the values of the given attributes. An optional protocol also
allows matching positional arguments.


OR pattern
----------
An `OR pattern` looks like ``[*x] | {"elems": [*x]}``. It matches if
any of its sub-patterns match. It uses the binding for the leftmost
pattern that matched.


Walrus pattern
--------------
A `walrus pattern` looks like ``d := datetime(year=2020, month=m)``. It
matches only if its sub-pattern also matches. It binds whatever the
sub-pattern match does, and also binds the named variable to the entire
object.


Guards
------


Recap
-----
* ``x`` - assign ``x = subject``
* ``'x'`` - test ``subject == 'x'``
* ``x.y`` - test ``subject == x.y``
* ``x()`` - test ``isinstance(subject, x)``
* ``{'x': 'y'}`` - test ``isinstance(subject, Mapping) and subject.get('x') == 'y'``
* ``['x']`` - test ``isinstance(subject, Sequence) and len(subject) == 1 and subject[0] == 'x'``
* Source: [#Hettinger2021]_


Use Case - 0x01
---------------
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['French'])

Use Case:

>>> language = input('What is your language?: ')  #input: 'French'
>>>
>>> match language:
...     case 'English': response = 'Hello'
...     case 'German':  response = 'Guten Tag'
...     case 'Spanish': response = 'Hola'
...     case 'Polish':  response = 'Witaj'
...     case _:         response = "I don't speak this language"
>>>
>>>
>>> print(response)
I don't speak this language


Use Case - 0x02
---------------
* HTTP Status

>>> status = 404
>>>
>>> match status:
...     case 400:             reason = 'Bad request'
...     case 401 | 403 | 405: reason = 'Not allowed'
...     case 404:             reason = 'Not found'
...     case 418:             reason = "I'm a teapot"
...     case _:               reason = 'Unexpected status'
>>>
>>>
>>> print(reason)
Not found


Use Case - 0x03
---------------
* HTTP Request

.. testsetup::

    >>> def handle_get(uri): ...
    >>> def handle_post(uri): ...
    >>> def handle_put(uri): ...
    >>> def handle_delete(uri): ...

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', path, version]:     handle_get(path)
...     case ['POST', path, version]:    handle_post(path)
...     case ['PUT', path, version]:     handle_put(path)
...     case ['DELETE', path, version]:  handle_delete(path)


Use Case - 0x04
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def make_damage(self): ...
...     def take_damage(self, dmg): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['make_damage', 10]
>>>
>>> match action:
...     case ['make_damage', value] if value > 0:
...         hero.make_damage()
...     case ['take_damage', value]:
...         hero.take_damage(value)


Use Case - 0x05
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def walk(self, direction, value): ...
...     def run(self, direction): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['walk', 'left', 10]
>>>
>>> match action:
...     case ['walk', ('up'|'down'|'left'|'right') as direction, value]:
...         hero.walk(direction, value)
...     case ['run', direction] if direction in ['up','down','left','right']:
...         hero.run(direction)


Use Case - 0x06
---------------
* Enum

Test Setup:

>>> class Keyboard:
...     def on_key_press(self): ...
>>>
>>> keyboard = Keyboard()

>>> class Game:
...     def quit(self): ...
...     def move_left(self): ...
...     def move_up(self): ...
...     def move_right(self): ...
...     def move_down(self): ...
>>>
>>> game = Game()

Use Case:

>>> from enum import Enum
>>>
>>>
>>> class Key(Enum):
...     ESC = 27
...     ARROW_LEFT = 37
...     ARROW_UP = 38
...     ARROW_RIGHT = 39
...     ARROW_DOWN = 40
>>>
>>> match keyboard.on_key_press():
...     case Key.ESC:          game.quit()
...     case Key.ARROW_LEFT:   game.move_left()
...     case Key.ARROW_UP:     game.move_up()
...     case Key.ARROW_RIGHT:  game.move_right()
...     case Key.ARROW_DOWN:   game.move_down()
...     case _: raise ValueError(f'Unrecognized key')
Traceback (most recent call last):
ValueError: Unrecognized key


Use Case - 0x07
---------------
>>> def myrange(*args, **kwargs):
...     if kwargs:
...         raise TypeError('myrange() takes no keyword arguments')
...
...     match len(args):
...         case 3:
...             start = args[0]
...             stop = args[1]
...             step = args[2]
...         case 2:
...             start = args[0]
...             stop = args[1]
...             step = 1
...         case 1:
...             start = 0
...             stop = args[0]
...             step = 1
...         case 0:
...             raise TypeError('myrange expected at least 1 argument, got 0')
...         case _:
...             raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
...
...     current = start
...     result = []
...
...     while current < stop:
...         result.append(current)
...         current += step
...
...     return result


Use Case - 0x08
---------------
>>> import json
>>> from datetime import date, time, datetime, timezone
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>>
>>> def encoder(value):
...     match value:
...         case date() | time() | datetime():
...             return value.isoformat()
...         case timedelta():
...             return value.total_seconds()
>>>
>>>
>>> json.dumps(DATA, default=encoder)
'{"firstname": "Mark", "lastname": "Watney", "born": "1994-10-12"}'


Use Case - 0x09
---------------
>>> import argparse
>>>
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('command', choices=['push', 'pull', 'commit'])
>>> args = parser.parse_args(['push'])
>>>
>>> match args.command:
...     case 'push':
...         print('pushing')
...     case 'pull':
...         print('pulling')
...     case _:
...         parser.error(f'{args.command!r} not yet implemented')
...
pushing


Further Reading
---------------
* https://peps.python.org/pep-0622/
* https://peps.python.org/pep-0636/


References
----------
.. [#Hettinger2021] Raymond Hettinger. Year: 2021. Retrieved: 2021-03-07. URL: https://twitter.com/raymondh/status/1361780586570948609?s=20

.. [#Shaw2022] Anthony Shaw. Write faster Python! Common performance anti patterns. Year: 2022. Retrieved: 2022-06-09. URL: https://youtu.be/YY7yJHo0M5I?t=1555

.. todo:: Assignments
