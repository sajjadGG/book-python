# output = {x: y
#     for x in range(0, 10)
#         for y in range(0, 10)
# }
#
# print(output)
#
#
#
#
# output = {}
#
# for x in range(0, 10):
#     for y in range(0, 10):
#         output[x] = y
#
# print(output)

FILE = r'iris-clean.csv'

with open(FILE) as file:
    file.readline()

    for line in file:
        line = line.strip().split(',')

        measurements = line[0:4]
        species = line[4]
