a = bool(False)
b = bool(True)

c = bool(0)
d = bool(0.0)
e = bool(-0)
f = bool(-0.0)

g = bool('a')
h = bool('.')
i = bool('0')
j = bool('0.0')
k = bool('')
l = bool(' ')

m = bool(int('0'))
n = bool(bool(float(str(-0))))

o = bool(-0.0+0.0j)
p = bool('-0.0+0.0j')


print(a)    # False
print(b)    # True
print(c)    # False
print(d)    # False
print(e)    # False
print(f)    # False
print(g)    # True
print(h)    # True
print(i)    # True
print(j)    # True
print(k)    # False
print(l)    # True
print(m)    # False
print(n)    # False
print(o)    # False
print(p)    # True
