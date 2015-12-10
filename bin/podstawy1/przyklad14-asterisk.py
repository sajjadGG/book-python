def foo(a, b, *args, **kwargs):
    print(locals())


foo(1, 2, **{'napiecie':10, 'natezenie': 20, 'moc': 3})

foo(
    1,
    2,
    napiecie=10,
    natezenie=20,
    moc=3)




def bar():
    return range(0, 5)

jeden, dwa, *reszta = bar()

print(jeden, dwa, reszta)




def foobar(a, b, *args):
    print(locals())

foobar(1, 2, 5, 7)


def foobar(a, b, **kwargs):
    print(locals())

foobar(1, 2, 5, 7)