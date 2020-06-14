DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

result = {}

for idx, titles in DATA.items():
    for title in titles:
        result[title] = str(idx)

print(result)


## Alternative solution
# result = {title: str(idx)
#           for idx, titles in DATA.items()
#               for title in titles}
