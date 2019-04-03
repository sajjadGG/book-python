DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

wynik = {}

for key, value in DATA.items():
    for education in value:
        wynik[education] = str(key)

## Alternatywnie
#
# wynik = {education: str(key)
#     for key, value in EDUCATION_GROUPS.items()
#         for education in value
# }

print(wynik)
# {
#   'Doctorate': '6',
#   'Prof-school': '6',
#   'Masters': '5',
#   'Bachelor': '5',
#   'Engineer': '5',
#   'HS-grad': '4',
#   'Junior High': '3',
#   'Primary School': '2',
#   'Kindergarten': '1'
# }
