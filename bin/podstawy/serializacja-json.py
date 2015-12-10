#!/usr/bin/env python3

import json

dane_w_formacie_python = [
    {'uczestnicy_szkolenia_grudzien_2015': ['Sylwia', 'Krzysztof', 'Sylwia', 'Aleksandra', 'Piotr', 'Sławomir',
                                            'Katarzyna', 'Jarosław']},
    {'samoloty': ['myśliwiec', 'toransportowy', 'pasażerski']},
    {
        'tekst': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'},
    {'cudzysłów': 'to jest cytat "Cycerona"'},
]

# print('Python: ', dane_w_formacie_python)
dane_w_formacie_json = json.dumps(dane_w_formacie_python)
# print('JSON:   ', dane_w_formacie_json)


with open('/tmp/tymczasowy', 'w') as file:
    file.write(dane_w_formacie_json)

with open('/tmp/tymczasowy') as file:
    zawartosc = file.read()
    # print('JSON:   ', zawartosc)
    na_powrot = json.loads(zawartosc)

# print('Python: ', na_powrot)


import pprint

pprint.pprint(na_powrot)
