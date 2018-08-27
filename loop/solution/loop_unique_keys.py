DATA = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Max', 'last_name': 'Peck', 'first_step': 1969},
    {'first_name': 'José', 'first_flight': 1961, 'agency': 'NASA'},
]

unique_keys = set()

for row in DATA:
    unique_keys.update(row.keys())

print(unique_keys)
