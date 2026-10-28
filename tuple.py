# TUPLE FUNCTIONS / METHODS

t = (10, 20, 30, 20, 40, 50, 20)

# 1. len()
print("Length:", len(t))

# 2. count()
print("Count of 20:", t.count(20))

# 3. index()
print("Index of 30:", t.index(30))

# 4. max()
print("Maximum:", max(t))

# 5. min()
print("Minimum:", min(t))

# 6. sum()
print("Sum:", sum(t))

# 7. sorted()
print("Sorted:", sorted(t))

# 8. tuple()
x = [1, 2, 3]
new_tuple = tuple(x)
print("List converted to tuple:", new_tuple)

# 9. Membership: in
print("30 is in tuple:", 30 in t)

# 10. Membership: not in
print("100 is not in tuple:", 100 not in t)