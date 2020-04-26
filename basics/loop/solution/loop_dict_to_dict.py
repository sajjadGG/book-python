INPUT = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

output = {}

for level, degrees in INPUT.items():
    for education in degrees:
        output[education] = str(level)

print(output)


## Alternative solution
# output = {education: str(level)
#     for level, degrees in INPUT.items()
#         for education in degrees
# }
