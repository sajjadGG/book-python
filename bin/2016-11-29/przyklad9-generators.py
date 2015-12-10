
nieparzyste_list_comp = [x*x for x in range(0, 30) if x % 2]

print(nieparzyste_list_comp)

print(nieparzyste_list_comp)


print('------')

nieparzyste_generator = (x*x for x in range(0, 30) if x % 2)

"""
for liczba in nieparzyste_generator:
    print(liczba)
"""

print(list(nieparzyste_generator))

print(list(nieparzyste_generator))
