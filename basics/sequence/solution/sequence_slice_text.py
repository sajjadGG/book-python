a = 'dr hab. inż. Jan Twardowski, prof. AATC'
b = 'gen. pil. Jan Twardowski'
c = 'Mark Watney, PhD'
d = 'lt. col. ret. Melissa Lewis'
e = 'dr n. med. Ryan Stone'
f = 'Ryan Stone, MD-PhD'
g = 'lt. col. Jan Twardowski\t'

print(a[13:-12])
print(b[10:])
print(c[:-5])
print(d[14:])
print(e[11:])
print(f[:-8])
print(g[9:-1])

print(f'>{g[9:-1]}<')
# >Jan Twardowski<
