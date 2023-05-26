# LISTS
a = [1, 2, 3, 4]
b = [2, 3, 4]

# Use ==, !=, <, > operators for list comparison
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

# Convert lists to sets for comparison
s1 = set(a)
s2 = set(b)
print(s1 == s2)
print(s1.union(s2))

# Sort before convert
sorted_a = sorted(a)
sorted_b = sorted(b)
print(sorted_a == sorted_b)

# Use all() to compare all elements
print(all(a_elem == b_elem for a_elem, b_elem in zip(a, b)))

# Use zip() to compare element-wise and find differences
diff = [(a_elem, b_elem) for a_elem, b_elem in zip(a, b) if a_elem != b_elem]
print(diff)

# TUPLES

# Use ==, !=, <, > operators for tuple comparison
a = (1, 2, 3, 4)
b = (3, 4, 2)

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

# Convert tuples to sets for comparison
s1 = set(a)
s2 = set(b)
print(s1 == s2)
print(s1.union(s2))

# Sort before convert
sorted_a = sorted(a)
sorted_b = sorted(b)
print(sorted_a == sorted_b)

# Use all() to compare all elements
print(all(a_elem == b_elem for a_elem, b_elem in zip(a, b)))

# Use zip() to compare element-wise and find differences
diff = [(a_elem, b_elem) for a_elem, b_elem in zip(a, b) if a_elem != b_elem]
print(diff)
