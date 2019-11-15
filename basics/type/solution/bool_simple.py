a = bool(1) == True                          # True
b = bool(0) == False                         # True
c = True == True                             # True
d = True != False                            # True
e = True or True                             # True
f = False and True                           # False
g = bool(bool(False) == False) or False      # True
h = None is None                             # True

print(a)                                     # True
print(b)                                     # True
print(c)                                     # True
print(d)                                     # True
print(e)                                     # True
print(f)                                     # False
print(g)                                     # True
print(h)                                     # True
