INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
         0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
         2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
         1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
         4, 8, 1, 9, 6, 3]

SMALL = [0, 1, 2]
MEDIUM = [3, 4, 5, 6]
LARGE = [7, 8, 9]

counter = {
    'small': 0,
    'medium': 0,
    'large': 0,
}

for digit in INPUT:
    if digit in SMALL:
        counter['small'] += 1
    elif digit in MEDIUM:
        counter['medium'] += 1
    elif digit in LARGE:
        counter['large'] += 1

print(counter)


# Alternative version
# INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
#          0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
#          2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
#          1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
#          4, 8, 1, 9, 6, 3]
#
# COUNTERS = [
#     {'name': 'small', 'range': [0, 1, 2], 'count': 0, 'digits': [], 'indexes': []},
#     {'name': 'medium', 'range': [3, 4, 5, 6, 7], 'count': 0, 'digits': [], 'indexes': []},
#     {'name': 'large', 'range': [8, 9], 'count': 0, 'digits': [], 'indexes': []},
#     {'name': 'even', 'range': [0, 2, 4, 6, 8], 'count': 0, 'digits': [], 'indexes': []},
#     {'name': 'odd', 'range': [1, 3, 5, 7, 9], 'count': 0, 'digits': [], 'indexes': []},
#     {'name': 'custom', 'range': [1, 2, 9], 'count': 0, 'digits': [], 'indexes': []},
# ]
#
# for idx, digit in enumerate(INPUT):
#     for counter in COUNTERS:
#         if digit in counter['range']:
#             counter['indexes'].append(idx)
#             counter['digits'].append(digit)
#             counter['count'] += 1
#
#
# print(COUNTERS)
