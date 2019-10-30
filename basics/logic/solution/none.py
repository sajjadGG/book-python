a = None is None  # True
b = None is not None  # False
c = bool(bool(None) is not bool(None)) == False  # True
d = (bool(bool(None) is not bool(None)) == False and bool(None))  # False
e = (bool(bool(None) is not bool(None)) == False and bool(None)) and (None is not None)  # False

print(a)  # True
print(b)  # False
print(c)  # True
print(d)  # False
print(e)  # False

