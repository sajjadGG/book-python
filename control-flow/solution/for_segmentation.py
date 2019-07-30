DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
        0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
        1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

counter = {
    'small': [],
    'medium': [],
    'large': [],
}

for digit in DATA:
    if 0 <= digit <= 2:
        counter['small'].append(digit)
    elif 3 <= digit <= 7:
        counter['medium'].append(digit)
    elif 8 <= digit <= 9:
        counter['large'].append(digit)

count_small = len(counter['small'])
count_medium = len(counter['medium'])
count_large = len(counter['large'])

print(f'Small: {count_small}')
print(f'Medium: {count_medium}')
print(f'Large: {count_large}')


## Alternative version
# DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
#         0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
#         2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
#         1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
#         4, 8, 1, 9, 6, 3]
#
# COUNTERS = [
#     {'name': 'small', 'range': range(0, 3), 'count': 0, 'digits': []},
#     {'name': 'medium', 'range': range(3, 8), 'count': 0, 'digits': []},
#     {'name': 'large', 'range': range(8, 10), 'count': 0, 'digits': []},
#     {'name': 'custom', 'range': [1, 5, 9], 'count': 0, 'digits': []},
# ]
#
# for digit in DATA:
#     for counter in COUNTERS:
#         if digit in counter['range']:
#             counter['digits'].append(digit)
#             counter['count'] += 1
#
#
# from pprint import pprint
# pprint(COUNTERS)
