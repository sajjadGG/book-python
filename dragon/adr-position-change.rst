Dragon ADR Position Change
==========================
* ADR - Architecture Design Records


Problem
-------
* Move dragon left by 10 and down by 20
* Move by setting absolute position or list of absolute positions
* Move by setting position
* Move by relative shifting (left, right, up, down)


Names
-----
* dragon.change_position()
* dragon.position_change()
* dragon.move()
* dragon.shift()
* dragon.fly_to()


Option 1
--------
>>> dragon.move(left=10, down=20)
>>> dragon.change_position(left=10, down=20)
>>> dragon.position_change(left=10, down=20)


Option 2
--------
>>> dragon.move(x=10, y=-20)
>>> dragon.move_to(x=10, y=20)


Option 3
--------
>>> dragon.move_x(10)
>>> dragon.move_y(20)


Option 4
--------
>>> dragon.move(10, 20)
>>> dragon.move_xy(10, 20)


Option 5
--------
>>> dragon.move((-10, 20))
>>> dragon.move_xy((-10, 20))


Option 6
--------
>>> dragon.move(dx=10, dy=-20)
>>> dragon.move(vertical=10, horizontal=-20)


Option 7
--------
* move(left, right, up, down)

>>> dragon.move(0, 10, 0, 20)
>>> dragon.move((0, 10, 0, 20))

>>> dragon.move([
...     (0, 10, 0, 20),
...     (0, 10, 0, 20)])


Option 8
--------
* move(horizontal, vertical)
* move by relative offset

>>> dragon.move([
...     (10, 20),
...     (10, 15)])


Option 9
--------
* move(x, y)
* move by setting absolute position

>>> dragon.move([
...     (10, 20),
...     (50, 120),
...     (5)])


Option 10
---------
>>> dragon.move({'x':50, 'y':120})

>>> dragon.move([
...     {'x':10, 'y':20},
...     {'x':10, 'y':15}])


Option 11
---------
>>> dragon.move({'left':50, 'down':120})

>>> dragon.move([
...     {'left':50, 'down':120},
...     {'left':50, 'right':120},
...     {'down':50}])



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


Option 13
---------
* move by setting absolute position

>>> dragon.move([
...     Point(x=10, y=20),
...     Point(x=10, y=15)])


Option 14
---------
>>> dragon.move([
...     {'direction': 'left', 'distance': 20},
...     {'direction': 'left', 'distance': 10},
...     {'direction': 'right', 'distance': 20}])


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


Option 16
---------
>>> dragon.move(x=-10, y=+20)
>>> dragon.move(dx=-10, dy=+20)
>>> dragon.change_position(left=-10, down=20)


Option 17
---------
>>> dragon.move(direction='left', distance=20)
>>> dragon.move(direction='right', distance=5)


Option 18
---------
>>> LEFT = 61  # keyboard key code
>>> dragon.move(direction=LEFT, distance=20)


Option 19
---------
>>> class Direction(Enum):
...     LEFT = 61
>>>
>>> dragon.move(direction=Direction.LEFT, distance=5)


Option 20
---------
>>> KEY_BINDING = {
...     'ARROW_UP': dragon.move_up,
...     'ARROW_DOWN': dragon.move_down,
...     'ARROW_LEFT': dragon.move_left,
...     'ARROW_RIGHT': dragon.move_right}

>>> def action(key, time):
...     return KEY_BINDING.get(key)(time)
>>>
>>> action('ARROW_UP', 5)


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

>>> db.execute_insert(...)
>>> db.execute_select()
>>> db.execute_create()
>>> db.execute_alter()
>>> db.execute_alter_table()
>>> db.execute_create_table()
>>> db.execute_create_database()

Use Case:

>>> read_csv('iris.csv', 'utf-8', ';', True)

>>> read_csv_with_encoding('iris.csv', 'utf-8')
>>> read_csv_with_delimiter('iris.csv', ';')
>>> read_csv_with_delimiter_and_encoding('iris.csv', ';', 'utf-8')

>>> read_csv('iris.csv')
...     .withEncoding('utf-8')
...     .withDelimiter(';')
...     .withVerbose(True)

>>> file = CSV()
>>> file.set_file('iris.csv')  # encapsulation?!
>>> file.set_encoding('utf-8')
>>> file.set_delimiter(';')


>>> read_csv('iris.csv', encoding='utf-8', delimiter=';', verbose=True)

>>> read_csv('iris.csv',
...          encoding='utf-8',
...          delimiter=';',
...          verbose=True)


Decision
--------
>>> dragon.move(left=10, down=20)

Alternative:

>>> dragon.change_position(left=10, down=20)
>>> dragon.position_change(left=10, down=20)

* Good: easy
* Good: verbose
* Good: extensible
