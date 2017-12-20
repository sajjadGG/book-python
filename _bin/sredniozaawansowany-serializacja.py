DATA = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan'},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961, 'first_step': 1969},
]


# Wykorzystując listę
fieldnames = []

for record in DATA:
    for key in record.keys():
        if key not in fieldnames:
            fieldnames.append(key)

print('list():', fieldnames)


# set(), podejście 1
# Wykorzystując zbiór, który deduplikuje za nas
fieldnames = set()

for record in DATA:
    for key in record.keys():
        fieldnames.add(key)

print('set(), podejście 1:', fieldnames)


# set(), podejście 2
# Wykorzystując zbiór, który deduplikuje za nas
fieldnames = set()

for key in [record.keys() for record in DATA]:
    fieldnames.update(key)

print('set(), podejście 2:', fieldnames)


# set(), podejście 3
# Wykorzystując zbiór, który deduplikuje za nas
fieldnames = set()

for record in DATA:
    fieldnames.update(record.keys())

print('set(), podejście 3:', fieldnames)


# set(), podejście 4
# Wykorzystując zbiór, który deduplikuje za nas
fieldnames = set()
fieldnames.update(key for key in record.keys() for record in DATA)
print('set(), podejście 4:', fieldnames)

