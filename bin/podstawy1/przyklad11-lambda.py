lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def parzystosc(x):
    if x % 2 == 0:
        return True
    else:
        return False


parzyste1 = filter(lambda x: x % 2 == 0, lista)
parzyste2 = filter(parzystosc, lista)

print(list(parzyste1))
print(list(parzyste2))
