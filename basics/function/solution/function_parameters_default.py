def default(a, b=None):
    if b is None:
        b = a

    print(f'{a=} {b=}')


default(1)
# a=1 b=1

default(2, 3)
# a=2 b=3
