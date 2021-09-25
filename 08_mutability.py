a = []
b = a

print(id(a))
print(id(b))

a.append(34)

print(b)

# ha tényleges másolat kell a listáról, akkor a .copy() metódust használd
b = a.copy()

print(id(a))
print(id(b))

a = 1995
b = 1995

print(id(a))
print(id(b))

b = 2342

print(id(a))
print(id(b))

# immutable: bool, int, float, tuple, string, frozenset
# mutable: list, set, dict