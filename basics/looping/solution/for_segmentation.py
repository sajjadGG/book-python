INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0, 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
         2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9, 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
         4, 8, 1, 9, 6, 3]

OUTPUT = {
    'small': 0,
    'medium': 0,
    'large': 0,
}

for digit in INPUT:
    if 0 <= digit <= 2:
        OUTPUT['small'] += 1
    elif 3 <= digit <= 7:
        OUTPUT['medium'] += 1
    elif 8 <= digit <= 9:
        OUTPUT['large'] += 1

print(OUTPUT)


## Alternative version
# INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
#          0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
#          2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
#          1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
#          4, 8, 1, 9, 6, 3]
#
# OUTPUT = [
#     {'name': 'small', 'range': range(0, 3), 'count': 0, 'digits': []},
#     {'name': 'medium', 'range': range(3, 8), 'count': 0, 'digits': []},
#     {'name': 'large', 'range': range(8, 10), 'count': 0, 'digits': []},
#     {'name': 'even', 'range': [0, 2, 4, 6, 8], 'count': 0, 'digits': []},
#     {'name': 'odd', 'range': [1, 3, 5, 7, 9], 'count': 0, 'digits': []},
#     {'name': 'custom', 'range': [1, 2, 9], 'count': 0, 'digits': []},
# ]
#
# for digit in INPUT:
#     for counter in OUTPUT:
#         if digit in counter['range']:
#             counter['digits'].append(digit)
#             counter['count'] += 1
#
#
# print(OUTPUT)
