def bar():
    raise NameError


def foo():
    try:
        bar()
    except NameError:
        print('Błąd nazwy zlapany')
    except SyntaxError:
        print('Błąd składni zlapany')


if __name__ == '__main__':
    foo()
