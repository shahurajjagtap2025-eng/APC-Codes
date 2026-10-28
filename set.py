s = {1, 2, 3}

s.add(4)
print(s)

s.remove(2)
print(s)

s.discard(3)
print(s)

s = {10, 20, 30}

x = s.pop()
print(x)
print(s)

s = {1, 2, 3}

s.clear()
print(s)

s = {1, 2, 3}

x = s.copy()
print(x)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))