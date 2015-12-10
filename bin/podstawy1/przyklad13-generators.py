


a = [x for x in range(0, 30)]
b = (x for x in range(0, 30))
c = {x for x in range(0, 30)}
d = list(x for x in range(0, 30))
e = tuple(x for x in range(0, 30))
f = set(x for x in range(0, 30))

print(x for x in range(0, 30))


ADDRESS_BOOK = [
    {'imie': 'Matt',
    'nazwisko': 'Harasymczuk',
    'ulica': 'Westpad',
    'miasto': 'Katwijk aan Zee',
    'kod_pocztowy': '2224',
    'wojewodztwo': 'Zuid-Holland',
    'panstwo': 'Netherlands'},

    {'imie': 'Angelika',
    'nazwisko': 'Jan',
    'ulica': 'Bial',
    'miasto': 'Warszawa',
    'kod_pocztowy': '02-370',
    'wojewodztwo': 'Mazowieckie',
    'panstwo': 'Polska'},
]


osoby = [{'imie': x['imie'], 'nazwisko': x['nazwisko']} for x in ADDRESS_BOOK]



#xyz = [MAP(x) for x in ZBIOR if FILTER(x)]




print(osoby)


# List Comprehension

def parzyste_f1(x):
    if x % 2 == 0:
        return True
    else:
        return False

def parzyste_f2(x):
    return x % 2 == 0


parzyste1 = [float(x) for x in range(0, 30) if x % 2 == 0]
parzyste2 = [float(x) for x in range(0, 30) if parzyste_f1(x)]


parzyste3 = []

for x in range(0, 30):
    if x % 2 == 0:
        parzyste3.append(float(x))


def parzyste_f3():
    parzyste = []

    for x in range(0, 30):
        if x % 2 == 0:
            parzyste.append(float(x))

    return parzyste


def parzyste_f4():
    for x in range(0, 30):
        if x % 2 == 0:
            yield float(x)


print(parzyste_f4())
a = parzyste_f4()

print('next1', a.__next__())
print('next2', a.__next__())
print('next3', a.__next__())
print('next4', a.__next__())


for liczba in parzyste_f4():
    print(liczba)



a = range(0, 30)


# Generator Expressions


liczby = (x for x in range(0, 30))
parzyste1 = (x for x in range(0, 30) if x % 2 == 0)

MAX = 30
parzyste1 = (x for x in range(0, MAX) if x % 2 == 0)

p = lambda a: (x for x in range(0, a) if x % 2 == 0)

def xxx(a):
    return (x for x in range(0, a) if x % 2 == 0)

p(2)
xxx(2)






parzyste2 = (x for x in range(0, a) if x % 2 == 0)


