DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan', 'age': 30},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
]

unique_keys = set()

for row in DATABASE:
    for key in row.keys():
        unique_keys.add(key)

print(unique_keys)