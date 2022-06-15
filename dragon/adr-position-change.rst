.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Position Change
==========================
* ADR - Architecture Design Records


Problem
-------
* Move dragon left by 10 and down by 20


Option 1
--------
>>> dragon.move(left=10, down=20)
>>> dragon.shift(left=10, down=20)
>>> dragon.fly(left=10, down=20)

* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position and moves
* Good: easy ``.move()``
* Bad: to use-case specific ``.fly()``, ``.shift()``


Option 2
--------
>>> dragon.change_position(left=10, down=20)
>>> dragon.position_change(left=10, down=20)

* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position and moves
* Bad: to complex for now ``.change_position()``, ``.position_change()``


Option 3
--------
>>> dragon.move(x=10, y=-20)
>>> dragon.move_to(x=10, y=20)

* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as velocity, surface, injuries

.. figure:: img/oop-architecture-mvc.png


Option 4
--------
>>> dragon.move_x(10)
>>> dragon.move_y(20)

* Good: extensible to 3D, just add another method
* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as velocity, surface, injuries


Option 5
--------
>>> dragon.move(10, 20)
>>> dragon.move_xy(10, 20)

* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as velocity, surface, injuries
* Bad: not extensible to 3D


Option 6
--------
>>> dragon.move((-10, 20))
>>> dragon.move_xy((-10, 20))

* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as velocity, surface, injuries
* Bad: not extensible to 3D


Option 7
--------
>>> dragon.move(dx=10, dy=-20)
>>> dragon.move(horizontal=10, vertical=-20)

* Good: encapsulation, object knows current position and moves
* Bad: controller computes final offset
* Bad: controller must know, right - add to ``x``, left - subtract ``y``


Option 8
--------
>>> dragon.move(0, 10, 0, 20)
>>> dragon.move((0, 10, 0, 20))

>>> dragon.move([
...     (0, 10, 0, 20),
...     (0, 10, 0, 20)])

* Good: there is only one method ``move()`` responsible for moving
* Bad: Python has keyword arguments, so use it
* Bad: require knowledge of an API
* Bad: not extensible to 3D

Example:

* ``move(left, right, up, down)``

Problem:

* ``check(True, False, True, None, 1)``

.. code-block:: css

    p {
      margin-top: 100px;
      margin-bottom: 100px;
      margin-right: 150px;
      margin-left: 80px;
    }

.. code-block:: css

    p {
      margin: 25px 50px 75px 100px; /* top, right, bottom, left */
    }

.. code-block:: css

    p {
      margin: 25px 50px 75px;  /* top, right-left, bottom */
    }

.. code-block:: css

    p {
      margin: 25px 50px;  /* top-bottom, right-left */
    }

.. code-block:: css

    p {
      margin: 25px;  /* top-right-bottom-left */
    }


Option 9
--------
>>> dragon.move([
...     (10, 20),
...     (10, 15)])

* Good: move by relative offset
* Bad: require knowledge of an API
* Bad: not extensible to 3D

Example:

* ``move(horizontal, vertical)``

Option 9
--------
>>> dragon.move([
...     (10, 20),
...     (50, 120),
...     (5)])

* Bad: move by setting absolute position
* Bad: require knowledge of an API
* Bad: not extensible to 3D

Example:

* ``move(x, y)``


Option 10
---------
>>> dragon.move({'x':50, 'y':120})

>>> dragon.move([
...     {'x':10, 'y':20},
...     {'x':10, 'y':15}])

* Bad: require knowledge of an API
* Bad: not extensible to 3D


Option 11
---------
>>> dragon.move({'left':50, 'down':120})

>>> dragon.move([
...     {'left':50, 'down':120},
...     {'left':50, 'right':120},
...     {'down':50}])

* Bad: require knowledge of an API
* Bad: not extensible to 3D


Option 12
---------
>>> dragon.move({'dx': 10, 'dy': 20})

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 0}])

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20}])

* Bad: require knowledge of an API


Option 13
---------
* move by setting absolute position

>>> dragon.move([
...     Point(x=10, y=20),
...     Point(x=10, y=15)])

* Good: extensible to 3D
* Bad: require knowledge of an API


Option 14
---------
>>> dragon.move([
...     {'direction': 'left', 'distance': 20},
...     {'direction': 'left', 'distance': 10},
...     {'direction': 'right', 'distance': 20}])

* Good: extensible to 3D
* Bad: require knowledge of an API


Option 15
---------
>>> x = dragon.x
>>> y = dragon.y
>>> dragon.move(x=x-10, y=y+20)

>>> current = dragon.position
>>> dragon.set_position(x=current.x-10, y=current.y+20)

>>> x = dragon.x - 10
>>> y = dragon.y + 20
>>> dragon.move(x=x, y=y)

>>> dragon.x -= 10
>>> dragon.y += 20

>>> dragon.position_x -= 10
>>> dragon.position_y += 20


* Good: extensible to 3D, just add ``z`` attribute
* Bad: encapsulation
* Bad: require knowledge of an API


Option 16
---------
>>> dragon.move(x=-10, y=+20)
>>> dragon.move(dx=-10, dy=+20)
>>> dragon.change_position(left=-10, down=20)

* Good: extensible to 3D
* Bad: business login in controller


Option 17
---------
>>> dragon.move(direction='left', distance=20)
>>> dragon.move(direction='right', distance=5)

* Good: explicit
* Good: verbose
* Good: extensible
* Good: extensible to 3D
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time


Option 18
---------
>>> LEFT = 61  # keyboard key code
... RIGHT = 61
... UP = 61
... DOWN = 61
>>>
>>> dragon.move(direction=LEFT, distance=20)

* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to chaotic
* Bad: to complex for now


Option 19
---------
>>> class Direction(Enum):
...     LEFT = 61
...     RIGHT = 61
...     UP = 61
...     DOWN = 61
>>>
>>>
>>> dragon.move(Direction.LEFT, distance=5)
>>> dragon.move(direction=Direction.LEFT, distance=5)

* Good: explicit
* Good: verbose
* Good: extensible
* Good: ordered
* Bad: to complex for now


Option 20
---------
>>> KEY_BINDING = {
...     'ARROW_UP': dragon.move_up,
...     'ARROW_DOWN': dragon.move_down,
...     'ARROW_LEFT': dragon.move_left,
...     'ARROW_RIGHT': dragon.move_right}
>>>
>>>
>>> def action(key, time):
...     return KEY_BINDING.get(key)(time)
>>>
>>>
>>> action('ARROW_UP', 5)

* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to complex for now


Option 21
---------
>>> dragon.move_left(10)
>>> dragon.move_right(10)
>>> dragon.move_upright(10)
>>> dragon.move_downright(10)
>>> dragon.move_downleft(10)
>>> dragon.move_upleft(10)
>>> dragon.move_left_down(10, 20)

Good, because:

>>> game.bind_key(Key.LEFT_ARROW, dragon.move_left)
>>> game.bind_key(Key.RIGHT_ARROW, dragon.move_right)

Bad, because:

>>> db.execute_select(SQL)
>>> db.execute_select_where(SQL)
>>> db.execute_select_order(SQL)
>>> db.execute_select_limit(SQL)
>>> db.execute_select_offset(SQL)
>>> db.execute_select_order_limit(SQL)
>>> db.execute_select_where_order_limit(SQL)
>>> db.execute_select_where_order_limit_offset(SQL)
>>> db.execute_insert(SQL)
>>> db.execute_insert_values(SQL)
>>> db.execute_alter(SQL)
>>> db.execute_alter_table(SQL)
>>> db.execute_alter_index(SQL)
>>> db.execute_create(SQL)
>>> db.execute_create_table(SQL)
>>> db.execute_create_index(SQL)
>>> db.execute_create_database(SQL)

Why not?:

>>> db.execute(SQL)

Use Case:

>>> read_csv('iris.csv', ';', 'utf-8', True)

>>> read_csv_with_encoding('iris.csv', 'utf-8')
>>> read_csv_with_delimiter('iris.csv', ';')
>>> read_csv_with_delimiter_encoding('iris.csv', ';', 'utf-8')
>>> read_csv_with_delimiter_encoding_verbose('iris.csv', ';', 'utf-8', True)

>>> read_csv('iris.csv')
...     .withEncoding('utf-8')
...     .withDelimiter(';')
...     .withVerbose(True)

>>> file = CSV()
>>> file.set_file('iris.csv')  # encapsulation?!
>>> file.set_encoding('utf-8')
>>> file.set_delimiter(';')
>>> file.set_verbose(True)

>>> read_csv('iris.csv', encoding='utf-8', delimiter=';', verbose=True)

>>> read_csv('iris.csv',
...          encoding='utf-8',
...          delimiter=';',
...          verbose=True)

* Bad: not extensible
* Bad: to complex for now


Decision
--------
>>> dragon.move(left=10, down=20)

* Good: easy
* Good: verbose
* Good: extensible (easy to convert to 3D)

Alternative, maybe in future:

>>> dragon.change_position(left=10, down=20)

* Good: consistent with ``set_position()``
* Good: verbose
* Good: extensible
* Bad: to complex for now
