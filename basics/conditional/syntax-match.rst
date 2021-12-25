Block Match
===========

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['French'])

    def handle_get(uri): ...
    def handle_post(uri): ...
    def handle_put(uri): ...
    def handle_delete(uri): ...

    class Hero:
        def move(self, direction, value): ...
        def make_damage(): ...
        def take_damage(_): ...
    hero = Hero()

    class Game:
        def quit(): ...
        def move_left(): ...
        def move_up(): ...
        def move_right(): ...
        def move_down(): ...
    game = Game()

    class Keyboard:
        def on_key_press(self): ...
    keyboard = Keyboard()


Rationale
---------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial


Syntax
------
>>> # doctest: +SKIP
... match <object>:
...     case <option>: <action>
...     case <option>: <action>
...     case <option>: <action>
...     case _: <default action>


Example
-------
>>> language = input('What is your language?: ')  # User input: 'French'
>>>
>>> match language:
...     case 'English': response = 'Hello'
...     case 'Russian': response = 'Здравствуйте'
...     case 'German':  response = 'Guten Tag'
...     case 'Polish':  response = 'Witaj'
...     case _:         response = "I don't speak this language"
>>>
>>>
>>> print(response)
I don't speak this language


Patterns
--------
The patterns listed here are described in more detail below, but summarized together in this section for simplicity:

    * A `literal pattern` is useful to filter constant values in a
      structure. It looks like a Python literal (including some values like
      ``True``, ``False`` and ``None``). It only matches objects equal to
      the literal, and never binds.

    * A `capture pattern` looks like x and is equivalent to an identical
      assignment target: it always matches and binds the variable with the
      given (simple) name.

    * The `wildcard pattern` is a single underscore: ``_``.  It always
      matches, but does not capture any variable (which prevents
      interference with other uses for ``_`` and allows for some
      optimizations).

    * A `constant value pattern` works like the literal but for certain named
      constants. Note that it must be a qualified (dotted) name, given the
      possible ambiguity with a capture pattern. It looks like ``Color.RED``
      and only matches values equal to the corresponding value. It never
      binds.

    * A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
      list unpacking. An important difference is that the elements nested
      within it can be any kind of patterns, not just names or sequences. It
      matches only sequences of appropriate length, as long as all the
      sub-patterns also match. It makes all the bindings of its sub-patterns.

    * A `mapping pattern` looks like ``{"user": u, "emails": [*es]}``. It
      matches mappings with at least the set of provided keys, and if all the
      sub-patterns match their corresponding values. It binds whatever the
      sub-patterns bind while matching with the values corresponding to the
      keys. Adding **rest at the end of the pattern to capture extra items
      is allowed.

    * A `class pattern` is similar to the above but matches attributes
      instead of keys. It looks like ``datetime.date(year=y, day=d)``. It
      matches instances of the given type, having at least the specified
      attributes, as long as the attributes match with the corresponding
      sub-patterns. It binds whatever the sub-patterns bind when matching
      with the values of the given attributes. An optional protocol also
      allows matching positional arguments.

    * An `OR pattern` looks like ``[*x] | {"elems": [*x]}``. It matches if
      any of its sub-patterns match. It uses the binding for the leftmost
      pattern that matched.

    * A `walrus pattern` looks like ``d := datetime(year=2020, month=m)``. It
      matches only if its sub-pattern also matches. It binds whatever the
      sub-pattern match does, and also binds the named variable to the entire
      object.


Use Case - 0x01
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


Use Case - 0x02
---------------
* HTTP Request

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', uri, version]:     handle_get(uri)
...     case ['POST', uri, version]:    handle_post(uri)
...     case ['PUT', uri, version]:     handle_put(uri)
...     case ['DELETE', uri, version]:  handle_delete(uri)


Use Case - 0x03
---------------
* Game Controller

>>> action = ['move', 'left', 10]
>>>
>>> match action:
...     case ['move', ('up'|'down'|'left'|'right') as direction, value]:
...         hero.move(direction, value)
...     case ['make_damage', value]:
...         hero.make_damage()
...     case ['take_damage', value]:
...         hero.take_damage(value)


Use Case - 0x04
---------------
* Enum

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
...     case _:
...         raise ValueError(f'Unrecognized key')


Use Case - 0x05
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


Further Reading
---------------
* https://www.python.org/dev/peps/pep-0636/


Assignments
-----------
.. todo:: Create assignments
