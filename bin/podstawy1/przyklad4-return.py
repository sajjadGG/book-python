
def foo1():
    return True

def foo2():
    return None

def foo3():
    return 'bar'

def foo4():
    return [10, 20]

def foo5():
    return foo1

def foo6():
    pass

def foo7():
    return 10, 20, 30, 5, 'a'

def foo8():
    return {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}

def foo9():
    return [
        {'imie': 'Matt', 'nazwisko': 'Harasymczuk'},
        {'imie': 'Matt', 'nazwisko': 'Harasymczuk'},
        {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}]


if __name__ == '__main__':

    napiece, natezenie, *args = foo7()

    napiecie, *_ = foo7()
    print(_)

