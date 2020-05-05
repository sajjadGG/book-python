import numpy as np

DATA = [
    ('x', 'y'),
    (-4.0, 0.0),
    (-3.0, 2.5),
    (-2.0, 2.0),
    (0.0, -2.0),
    (2.0, 0.0),
    (3.0, 7.0)
]

header, *data = DATA

x = [x for x, y in data]
y = [y for x, y in data]
a = np.polyfit(x, y, deg=3)

print(a)
# [ 0.25  0.75 -1.5  -2.  ]


## Alternative
header, *data = DATA
x = []
y = []

for coord_x, coord_y in data:
    x.append(coord_x)
    y.append(coord_y)

a = np.polyfit(x, y, deg=3)

print(a)
# [ 0.25  0.75 -1.5  -2.  ]
