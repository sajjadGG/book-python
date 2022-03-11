Dragon ADR Position Change
==========================


Rationale
---------
* ADR - Architecture Design Records
* Move dragon left by 10 and down by 20


Possibilities
-------------
>>> dragon.move(left=10, down=20)  # good

>>> dragon.change_position(left=10, down=20)  # good

>>> dragon.move_left(10)
>>> dragon.move_right(10)
>>> dragon.move_upright(10)
>>> dragon.move_downright(10)
>>> dragon.move_downleft(10)
>>> dragon.move_upleft(10)
>>> dragon.move_left_down(10, 20)


game.bind_key(Key.LEFT_ARROW, dragon.move_left)
game.bind_key(Key.RIGHT_ARROW, dragon.move_right)


db.execute(SQL)

db.execute_insert(...)
db.execute_select()
db.execute_create()
db.execute_alter()
db.execute_alter_table()
db.execute_create_table()
db.execute_create_database()

read_csv('iris.csv', encoding='utf-8', delimiter=';', verbose=True)

read_csv('iris.csv',
         encoding='utf-8',
         delimiter=';',
         verbose=True,
         parse_dates=['...'])


read_csv('iris.csv', 'utf-8', ';', True)

read_csv('iris.csv')
    .withEncoding('utf-8')
    .withDelimiter(';')
    .withVerbose(True);


file = CSV()
file.set_file('iris.csv')  # błąd enkapsulacji
file.set_encoding('utf-8')
file.set_delimiter(';')




>>> dragon.move(0, 10, 0, 20)

>>> dragon.move([
...     (0, 10, 0, 20),
...     (0, 10, 0, 20)])

>>> dragon.move(dx=10, dy=-20)
>>> dragon.move(vertical=10, horizontal=-20)

>>> dragon.move(x=10, y=-20)

>>> dragon.move_x(10)
>>> dragon.move_y(20)

>>> dragon.move_to(x=10, y=20)
>>> dragon.move_xy(10, 20)

>>> dragon.move({'x':50, 'y':120})

>>> dragon.move({'left':50, 'down':120})

>>> dragon.move([
...     {'left':50, 'down':120},
...     {'left':50, 'right':120},
...     {'down':50}])

>>> dragon.move([
...     (10, 20),
...     (50, 120),
...     (5)])

>>> dragon.move([
...     (10, 20),
...     (10, 15)])

>>> dragon.move([
...     {'x':10, 'y':20},
...     {'x':10, 'y':15}])

>>> dragon.move([
...     Point(x=10, y=20),
...     Point(x=10, y=15)])

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

>>> dragon.move(x=-10, y=+20)

>>> dragon.move(dx=-10, dy=+20)

>>> dragon.change_position(left=-10, down=20)
>>> dragon.change_position((-10, 20))

>>> dragon.move([
...     (-10, 20),
...     (-10, 20),
...     (-10, 20)])

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20},])

>>> dragon.move([
...     {'left': -10, 'down': 20},
...     {'left': -10, 'right': 20},])

>>> dragon.move(direction='left', distance=20)

>>> dragon.move(direction='right', distance=5)

>>> LEFT = 61
>>> dragon.move(direction=LEFT, distance=20)

>>> class Direction(Enum):
...     LEFT = 61
>>>
>>> dragon.move(direction=Direction.LEFT, distance=5)

>>> dragon.move([
...     {'direction': 'left', 'distance': 20},
...     {'left': -10, 'right': 20},])

>>> KEY_BINDING = {
...     'ARROW_UP': dragon.move_up,
...     'ARROW_DOWN': dragon.move_down,
...     'ARROW_LEFT': dragon.move_left,
...     'ARROW_RIGHT': dragon.move_right}

>>> def action(key, time):
...     return KEY_BINDING.get(key)(time)
>>>
>>> action('ARROW_UP', 5)
