DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

output = {}

for key, value in DATA.items():
    for education in value:
        output[education] = str(key)

print(output)


## Alternative version
# output = {education: str(key)
#     for key, value in DATA.items()
#         for education in value
# }
