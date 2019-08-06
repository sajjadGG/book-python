expected = 'Jana III Sobieskiego'

a = 'ul Jana III SobIESkiego'
b = '\tul. Jana trzeciego Sobieskiego'
c = 'ulicaJana III Sobieskiego'
d = 'UL. JANA 3 \nSOBIESKIEGO'
e = 'UL. jana III SOBiesKIEGO'
f = 'ULICA JANA III SOBIESKIEGO  '
g = 'ULICA. JANA III SOBIeskieGO'
h = ' Jana 3 Sobieskiego  '
i = 'Jana III\tSobieskiego '


a = a.strip().upper().replace('UL', '').strip().title().replace('Iii', 'III')
b = b.strip().upper().replace('UL.', '').strip().title().replace('Trzeciego', 'III')
c = c.strip().upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
d = d.strip().upper().replace('UL.', '').strip().title().replace('\n', '').replace('3', 'III')
e = e.strip().upper().replace('UL.', '').strip().title().replace('Iii', 'III')
f = f.strip().upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
g = g.strip().upper().replace('ULICA.', '').strip().title().replace('Iii', 'III')
h = h.strip().upper().replace('3', 'III').strip().title().replace('Iii', 'III')
i = i.strip().upper().replace('\t', ' ').strip().title().replace('Iii', 'III')


print(f'{a == expected}\t j: "{a}"')
print(f'{b == expected}\t b: "{b}"')
print(f'{c == expected}\t c: "{c}"')
print(f'{d == expected}\t d: "{d}"')
print(f'{e == expected}\t e: "{e}"')
print(f'{f == expected}\t f: "{f}"')
print(f'{g == expected}\t g: "{g}"')
print(f'{h == expected}\t h: "{h}"')
print(f'{i == expected}\t i: "{i}"')
