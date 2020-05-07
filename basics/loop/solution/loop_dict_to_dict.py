DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

result = {}

for level, degrees in DATA.items():
    for education in degrees:
        result[education] = str(level)

print(result)


## Alternative solution
# result = {education: str(level)
#     for level, degrees in DATA.items()
#         for education in degrees
# }
